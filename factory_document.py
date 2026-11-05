# Factory Pattern - Document Creation System

class Document:
    def create(self):
        pass


class PDF(Document):
    def create(self):
        print("PDF document created.")


class Word(Document):
    def create(self):
        print("Word document created.")


class Excel(Document):
    def create(self):
        print("Excel document created.")


class DocumentFactory:
    @staticmethod
    def get_document(choice):
        if choice == "pdf":
            return PDF()
        elif choice == "word":
            return Word()
        elif choice == "excel":
            return Excel()
        else:
            return None


choice = input("Enter document (pdf/word/excel): ").lower()

document = DocumentFactory.get_document(choice)

if document:
    document.create()
else:
    print("Invalid document type.")
```