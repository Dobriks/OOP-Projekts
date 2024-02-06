import pandas as pd

class Salidzinajums:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)

    def kom_salidzinajums(self, team_name, year1, year2):
    
        team_year1 = self.df[(self.df['gads'] == year1) & (self.df['komanda'] == team_name)]
        team_year2 = self.df[(self.df['gads'] == year2) & (self.df['komanda'] == team_name)]

        if team_year1.empty or team_year2.empty:
            raise ValueError(f"Tu neizvēlējies komandu")

            
        print(f"Komandas statistika {team_name}, {year1}.gadā:")
        print(team_year1)

        print(f"\nKomandas statistika {team_name}, {year2}. gadā:")
        print(team_year2)

            
        common_columns = set(self.df.columns) - set(['gads', 'komanda'])

        for column in common_columns:
            stat_year1 = team_year1[column].mean()
            stat_year2 = team_year2[column].mean()

            print(f"\nSalīdzinājums {column}:")
            print(f"{year1}: {stat_year1}")
            print(f"{year2}: {stat_year2}")

            if stat_year1 > stat_year2:
                print(f"{year1} Ir augstāki vidējie '{column}'.")
            elif stat_year1 < stat_year2:
                print(f"{year2} Ir augstāki vidējie '{column}'.")
            else:
                print(f"Vidējais '{column}' abos gados ir vienādas.")

