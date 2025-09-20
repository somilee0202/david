import json

def main():
    try:
        with open("mission_computer_main.log", "r", encoding="utf-8") as f:
            content = f.read()
            print("====== 파일 내용 ======")
            print(content)
            print("=====================\n")

        lines = content.splitlines()

        timestamp = []
        event = []
        message = []

        for line in lines[1:]:
            parses = line.split(',', 3)

            if len(parses) < 3:
                continue

            timestamp.append(parses[0].strip())
            event.append(parses[1].strip())
            message.append(parses[2].strip())

        timestamp.sort(reverse=True)
        event.sort()
        message.sort()

        print("====== timestamp ======")
        for t in timestamp:
            print(t)
        print("=====================\n")

        print("====== message ======")
        for m in message:
            print(m)
        print("=====================\n")

        data = {
            "timestamp": timestamp,
            "event": event,
            "message": message
        }

        # JSON 파일로 저장
        with open("mission_computer_main.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)


    except FileNotFoundError:
        print("ERROR: 파일을 찾을 수 없습니다.")
    except UnicodeDecodeError:
        print("ERROR: 파일을 UTF-8로 디코딩할 수 없습니다.")

if __name__ == "__main__":
    main()