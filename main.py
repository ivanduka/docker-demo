from ctypes.util import find_library
import camelot
import os

if __name__ == "__main__":
    id = os.getenv('FILE_ID')
    if id == None:
      raise Exception('Must have FILE_ID environmental variable to work')
    url = f'https://apps.cer-rec.gc.ca/REGDOCS/File/Download/{id}'
    tables = camelot.read_pdf(url)
    tables.export('foo.csv', f='csv')
    print(os.listdir())
    print("Done.")
