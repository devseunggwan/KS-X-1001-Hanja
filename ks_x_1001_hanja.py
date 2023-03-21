"""
MIT License

Copyright (c) 2023 devSeungGwan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class KsX1001HanjaVariable:
    """KS X 1001:2004 규격에서 지정해놓은 인코딩 범위를 지정해놓은 클래스입니다."""

    def __init__(self):
        self.list_ks_x_1001_1: list = ["c", "d", "e", "f"]
        self.dict_ks_x_1001_2: dict = {
            "c": ["a", "b", "c", "d", "e", "f"],
            "d": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            ],
            "e": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            ],
            "f": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d"],
        }
        self.list_ks_x_1001_3: list = ["a", "b", "c", "d", "e", "f"]
        self.list_ks_x_1001_4: list = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]


class KsX1001Hanja(KsX1001HanjaVariable):
    """KS X 1001:2004 규격에 맞는 한자 리스트를 생성하는 클래스입니다.
    * KS X 1001:2004 https://ko.wikipedia.org/wiki/KS_X_1001
    * KS X 1001:2004 한자 리스트: https://namu.wiki/w/%ED%95%9C%EC%9E%90/KS%20X%201001
    """

    def __init__(self):
        super().__init__()
        self.ks_x_1001_hanja: list = []

    def initialize_variable(self):
        """한자를 담는 변수를 초기화합니다."""
        self.ks_x_1001_hanja = []

    @staticmethod
    def write_text(path_output: str, texts: list):
        """한자 리스트를 파일로 저장합니다.

        Args:
            path_output (str): 출력하려는 파일 이름(경로)
            texts (list): 출력하려는 한자 리스트
        """
        with open(path_output, "w", encoding="utf-8") as file:
            for text in texts:
                file.write(f"{text}\n")

    def __call__(self, path_output: str = "output.txt"):
        self.initialize_variable()

        for ks_x_1001_1 in self.list_ks_x_1001_1:
            for kx_x_1001_2 in self.dict_ks_x_1001_2[ks_x_1001_1]:
                for ks_x_1001_3 in self.list_ks_x_1001_3:
                    for ks_x_1001_4 in self.list_ks_x_1001_4:
                        hanja = f'b"\\x{ks_x_1001_1}{kx_x_1001_2}\\x{ks_x_1001_3}{ks_x_1001_4}"'
                        hanja = literal_eval(hanja)
                        hanja = hanja.decode("euc-kr")
                        self.ks_x_1001_hanja.append(hanja)

        self.write_text(path_output=path_output, texts=self.ks_x_1001_hanja)

    def __len__(self):
        return len(self.ks_x_1001_hanja)
