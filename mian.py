import requests
import subprocess
def is_connected():
    try:
        # 嘗試發送一個 GET 請求到 Google
        response = requests.get("http://www.google.com", timeout=3)
        return True if response.status_code == 200 else False
    except requests.ConnectionError:
        print("無法連接到網路")
        return False
def open_network_settings():
    try:
        # 使用 subprocess 模組執行 Windows 命令來打開網路設定視窗
        subprocess.run('start ms-settings:network-status', shell=True, check=True)
        print("已打開網路設定視窗")
    except subprocess.CalledProcessError as e:
        print(f"無法打開網路設定視窗: {e}")

# 檢查網路連線
if is_connected():
    open_network_settings()
    print("網路已連接")

else:

    print("無網路連線")
