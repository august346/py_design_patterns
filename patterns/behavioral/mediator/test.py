import unittest

from . import Button, Checkbox, TextBox, DialogMediator


class TestMediator(unittest.TestCase):
    def setUp(self):
        self.mediator = DialogMediator()

        self.button1 = Button(name="Button1")
        self.checkbox1 = Checkbox(name="Checkbox1")
        self.textbox1 = TextBox(name="TextBox1")

        self.mediator.register(self.button1)
        self.mediator.register(self.checkbox1)
        self.mediator.register(self.textbox1)

    def test_button_click(self):
        with self.assertLogs('patterns.behavioral.mediator.pattern', level='INFO') as log:
            self.button1.click()
            self.assertIn("Button1 clicked.", log.output[0])
            self.assertIn("Button button_clicked by Button1. Updating other components...", log.output[1])
            self.assertIn("Checkbox1 updated due to button_clicked.", log.output[2])
            self.assertIn("TextBox1 updated due to button_clicked.", log.output[3])

    def test_checkbox_check(self):
        with self.assertLogs('patterns.behavioral.mediator.pattern', level='INFO') as log:
            self.checkbox1.check()
            self.assertIn("Checkbox1 checked.", log.output[0])
            self.assertIn("Checkbox checkbox_checked by Checkbox1. Updating other components...", log.output[1])
            self.assertIn("Button1 updated due to checkbox_checked.", log.output[2])
            self.assertIn("TextBox1 updated due to checkbox_checked.", log.output[3])


if __name__ == '__main__':
    unittest.main()
