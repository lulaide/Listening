import whisper
import requests
import os

# 加载 Whisper 模型
model = whisper.load_model("base")  # 可以选择 "tiny", "base", "small", "medium", "large"

def download_audio(url, output_path="audio.mp3"):
    """从指定的 URL 下载音频文件"""
    response = requests.get(url, stream=True)
    if response.status_code != 404:
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        return True
    else:
        print("无法下载音频文件，请检查链接。")
        return False

def transcribe_audio(audio_path):
    """转录音频为文本"""
    try:
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"转录失败: {e}")
        return None

if __name__ == "__main__":
    print("请输入音频链接，输入 'exit' 退出程序：")
    while True:
        url = input("音频链接: ").strip()
        if url.lower() == "exit":
            print("程序已退出。")
            break
        
        # 下载音频文件
        audio_file = "audio.mp3"
        if download_audio(url, audio_file):
            print("音频文件下载成功，开始转录...")
            
            # 转录音频
            transcript = transcribe_audio(audio_file)
            if transcript:
                print("转录文本：")
                print(transcript)
            else:
                print("转录失败，请检查音频文件。")
        else:
            print("音频文件下载失败，请检查链接是否有效。")
        
        print("\n等待下一个输入...")
