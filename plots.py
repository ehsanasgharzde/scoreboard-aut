from turtle import width
import pandas
import seaborn
import datetime
import matplotlib.pyplot


class Plots:
    def __init__(self):
        customize = {"axes.spines.right": False, "axes.spines.top": False}
        seaborn.set_theme(rc=customize, style="ticks")

    def calculate(self, dataset: pandas.DataFrame) -> pandas.DataFrame:
        axis = {
            "team": [],
            "score": []
        }
        
        for team in dataset.name.values.tolist():
            info = dataset.loc[dataset.name == team].drop(["name"], axis=1).values.tolist()
            score = sum(info[0])

            axis["team"].append(team)
            axis["score"].append(score)

        axis = pandas.DataFrame(axis)

        return axis

    def save(self, axis: pandas.DataFrame) -> str:
        seaborn.barplot(data=axis, x="team", y="score", color="blue", errcolor="blue", errwidth=0)

        date, time = str(datetime.datetime.now()).split()
        year, month, day = date.split("-")
        hour, minute, second = time.split(":")

        matplotlib.pyplot.savefig(f"plots/team-score-D{year}{month}{day}-T{hour}{minute}.png", dpi=300)
        path = f"plots/team-score-D{year}{month}{day}-T{hour}{minute}.png"

        return path
