import unittest
from typing import Type

from parameterized import parameterized

from . import PDFDocument, WordDocument, Document


class TestTemplateMethod(unittest.TestCase):
    @parameterized.expand(
        [
            (PDFDocument, [
                "Opening PDF document.",
                "Writing PDF content.",
                "Adding metadata to PDF.",
                "Saving PDF document.",
                "Closing PDF document."
            ]),
            (WordDocument, [
                "Opening Word document.",
                "Writing Word content.",
                "Adding metadata to Word document.",
                "Saving Word document.",
                "Closing Word document."
            ]),
        ]
    )
    def test(self, builder: Type[Document], logs: list[str]):
        document = builder()

        with self.assertLogs('patterns.behavioral.template_method.pattern', level='INFO') as log:
            document.create_document()

            self.assertEqual(len(log.output), len(logs), "Unexpected number of log entries.")

            for ind, text in enumerate(logs):
                self.assertIn(text, log.output[ind])


if __name__ == '__main__':
    unittest.main()
