import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication

import catornot


app = QApplication(sys.argv)


class WindowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.basic_invalid_directory = ".\\tests\\images\\basic_invalid"
        self.advanced_invalid_directory = ".\\tests\\images\\advanced_invalid"
        self.basic_valid_directory = ".\\tests\\images\\basic_valid"
        self.advanced_valid_directory = ".\\tests\\images\\advanced_valid"
        self.window = catornot.Window()

    def test_defaults(self):
        self.assertEqual(self.window.title, "Is Cat Or Not")
        self.assertEqual(self.window.top, 200)
        self.assertEqual(self.window.left, 500)
        self.assertEqual(self.window.width, 400)
        self.assertEqual(self.window.height, 300)
        self.assertEqual(self.window.imagePathGen, "")
        self.assertEqual(self.window.canCheck, False)
        self.assertEqual(self.window.newLabel.font().family(), "Times")
        self.assertEqual(self.window.newLabel.font().bold(), True)
        self.assertEqual(self.window.btn1.text(), "Open Image")
        self.assertEqual(self.window.btn2.text(), "Check Image")
        self.assertEqual(self.window.btn3.text(), "Advantage Check Image")

    def test_checkImage_cat(self):
        self.window.canCheck = True
        for file in os.scandir(self.basic_valid_directory):
            with self.subTest(file=file):
                self.window.imagePathGen = file.path
                self.window.checkImage()
                self.assertEqual(self.window.newLabel.text(), "Cat is in the picture!")

    def test_checkImage_no_cat(self):
        self.window.canCheck = True
        for file in os.scandir(self.basic_invalid_directory):
            with self.subTest(file=file):
                self.window.imagePathGen = file.path
                self.window.checkImage()
                self.assertEqual(self.window.newLabel.text(), "Cat is not in picture\n Try the 'Advantage Check "
                                                              "Image' to be sure")

    def test_checkImage_no_image(self):
        self.window.checkImage()
        self.assertEqual(self.window.newLabel.text(), "Enter an image to check")

    def test_advantageCheck_cat(self):
        self.window.canCheck = True
        for file in os.scandir(self.advanced_valid_directory):
            with self.subTest(file=file):
                self.window.imagePathGen = file.path
                self.window.advantageCheck()
                self.assertEqual(self.window.newLabel.text(), "Cat is in the picture!")

    def test_advantageCheck_no_cat(self):
        self.window.canCheck = True
        for file in os.scandir(self.advanced_invalid_directory):
            with self.subTest(file=file):
                self.window.imagePathGen = file.path
                self.window.advantageCheck()
                self.assertEqual(self.window.newLabel.text(), "Cat is not in picture")

    def test_advantageCheck_no_image(self):
        self.window.advantageCheck()
        self.assertEqual(self.window.newLabel.text(), "Enter an image to check")

    # żeby to niżej działało trzeba by było osobne foldery porobić, a mi się nie chce. ale zostawiam dla potomnych

    # def test_Retina_isCat_valid(self):
    #     for file in os.scandir(self.valid_directory):
    #         with self.subTest(file=file):
    #             self.window.imagePathGen = file.path
    #             self.assertEqual(self.window.isCat("Retina"), "cat")
    #
    # def test_Retina_isCat_invalid(self):
    #     for file in os.scandir(self.invalid_directory):
    #         with self.subTest(file=file):
    #             self.window.imagePathGen = file.path
    #             self.assertEqual(self.window.isCat("Retina"), None)
    #
    # def test_YOLO_isCat_valid(self):
    #     for file in os.scandir(self.valid_directory):
    #         with self.subTest(file=file):
    #             self.window.imagePathGen = file.path
    #             self.assertEqual(self.window.isCat("YOLO"), "cat")
    #
    # def test_YOLO_isCat_invalid(self):
    #     for file in os.scandir(self.invalid_directory):
    #         with self.subTest(file=file):
    #             self.window.imagePathGen = file.path
    #             self.assertEqual(self.window.isCat("YOLO"), None)
    #
    # def test_tinyYOLO_isCat_valid(self):
    #     for file in os.scandir(self.valid_directory):
    #         with self.subTest(file=file):
    #             self.window.imagePathGen = file.path
    #             self.assertEqual(self.window.isCat("tinyYOLO"), "cat")
    #
    # def test_tinyYOLO_isCat_invalid(self):
    #     for file in os.scandir(self.invalid_directory):
    #         with self.subTest(file=file):
    #             self.window.imagePathGen = file.path
    #             self.assertEqual(self.window.isCat("tinyYOLO"), None)


if __name__ == '__main__':
    unittest.main()