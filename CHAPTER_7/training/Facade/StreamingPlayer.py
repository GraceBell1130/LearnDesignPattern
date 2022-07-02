class StreamingPlayer():
    def __init__(self, description: str) -> None:
        self.description: str = description;
        self.currentChapter: int = 0
        self.movie: str = ""

    def __str__(self) -> str:
        return self.description

    def on(self) -> None:
        print(f"{self.description}가 켜졌습니다.")

    def off(self) -> None:
        print(f"{self.description}가 꺼졌습니다.")

    def play(self, movie: str) -> None:
        self.movie = movie;
        self.currentChapter = 0;
        print(f"{self.description}에서 \"{movie}\"를 재생합니다.")

    def playChpater(self, chapter: int) -> None:
        if self.movie is "":
            print(f"{self.description}는 영화가 선택되어있지 않아 {chapter}를 실행할 수 없습니다.")
        else:
            self.currentChapter = chapter;
            print(f"{self.description}에서 \"{self.movie}\"의 {self.currentChapter}를 재생합니다.")

    def stop(self) -> None:
        self.currentChapter = 0;
        print(f"{self.description}에서 \"{self.movie}\" 재생을 종료합니다.")

    def pause(self) -> None:
        print(f"{self.description}에서 \"{self.movie}\"를 정지합니다.")

    def setTwoChannelAudio(self) -> None:
        print(f"{self.description}를 투 채널 오디오로 설정합니다.")

    def setSurroundAudio(self) -> None:
        print(f"{self.description}를 서라운드 채널 오디오로 설정합니다.")
