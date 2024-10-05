"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import argparse
import logging
logging.basicConfig(level=logging.INFO,filename="test.log", filemode="w", format="%(message)s")


class cleaner:
    def _init_(self)-> None:
        pass

    def load_data(self) -> None:
        self.df = pd.read_csv(self.name)
        pass


    def fill_missing(self):
        self.df.Age.fillna(data.Age.mean(), inplace=True)
        self.df.Fare.fillna(1, inplace=True)
        self.df.Cabin.fillna("NA", inplace=True)

    def removing_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def age_bins(self):
        age_bins = [0, 18,25, 40, 60, 100]
        df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=['<18','18-25','25-40', '40-60', '60+'])
        print(pd.pivot_table(df, index='Age Group', columns='Survived', values='Ticket',aggfunc='count'))
        print()

    def map_embarked(self):
        embarked_mapping = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
        self.df['Embarked'] = data['Embarked'].map(embarked_mapping)

    def family_size(self):
        self.df['FamilySize'] = self.df['SibSp'] + self.df['Parch']
        return self.df




def main():
  parser = argparse.ArgumentParser(description="Titanic Data Analysis")
  parser.add_argument('--file', type=str, required=True, help="Path to the Titanic Data Analysis csv file.")
  args = parser.parse_args()

  titanic = TitanicCleaner(args.file)
  # logging.INFO("Load Titanic data and analyze missing values for the specified column")
  titanic.load_data()
  titanic.fill_missing_value()
  titanic.remove_duplicate()
  titanic.grouped_age()
  titanic.family_size()
  titanic.map_embarked_column()

if __name__ == "__main__":
  x = Titanic_cleaner()
  w= x.load_data()
  
"""


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import argparse
import logging
logging.basicConfig(level=logging.INFO,filename="test.log", filemode="w", format="%(message)s")


class cleaner:
    def _init_(self)-> None:
        pass

    def load_data(self) -> None:
        self.df = pd.read_csv(self.name)
        pass


    def fill_missing(self):
        self.df.Age.fillna(data.Age.mean(), inplace=True)
        self.df.Fare.fillna(1, inplace=True)
        self.df.Cabin.fillna("NA", inplace=True)

    def removing_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def age_bins(self):
        age_bins = [0, 18,25, 40, 60, 100]
        df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=['<18','18-25','25-40', '40-60', '60+'])
        print(pd.pivot_table(df, index='Age Group', columns='Survived', values='Ticket',aggfunc='count'))
        print()

    def map_embarked(self):
        embarked_mapping = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
        self.df['Embarked'] = data['Embarked'].map(embarked_mapping)

    def family_size(self):
        self.df['FamilySize'] = self.df['SibSp'] + self.df['Parch']
        return self.df


        
if __name__ == "__main__":
     ap = argparse.ArgumentParser()
     ap.add_argument











































"""
if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   x=cleaner()
   x.age_bins
   parser.add_argument('filename')
   arguments = parser.parse_args()
   print(arguments)
"""




































































































































































"""
def main():
    parser = argparse.ArgumentParser(description='Clean Titanic data.')
    parser.add_argument('tested.csv', help='Path to the Titanic data CSV file.')
    parser.add_argument('--output_file', help='Path to save the cleaned data CSV file.')
    parser.add_argument('--fill_missing', action='store_true', help='Fill missing values.')
    parser.add_argument('--remove_duplicates', action='store_true', help='Remove duplicate rows.')
    parser.add_argument('--calculate_family_size', action='store_true', help='Calculate family size.')
    parser.add_argument('--map_embarked', action='store_true', help='Map embarked codes to port names.')
    args = parser.parse_args()

    cleaner = Titanic_Cleaner.py(args.input_file)
    cleaner.load_data()

    if args.fill_missing:
        cleaner.fill_missing()
    if args.remove_duplicates:
        cleaner.removing_duplicates()
    if args.calculate_family_size:
        cleaner.calculate_family_size()
    if args.map_embarked:
        cleaner.map_embarked()

    if args.output_file:
        cleaner.df.to_csv(args.output_file, index=False)
    else:
        print(cleaner.df)


if __name__ == '__main__':
    main()
"""