from TerminalBasics import createtable

titles = ["Employee ID", "First Name", "Last name", "Salary ($)", "Hired Date"]
r1 = [1, "Eugene", "Krab", 1500, "2023-01-20"]
r2 = [2, "Squidward", "", 1000, "2023-01-19"]
r3 = [3, "Maria", "Malkin", "", "2023-01-19"]
r4 = [4, "Bob", "Marley", 2000, "2023-02-02"]
r5 = [5, "Lev", "Tolstoy", 3000, "2023-02-02"]
r6 = [6, "Mahmut", "Tuncer", 12000, "2024-12-01"]

createtable(titles, r1, r2, r3, r4, r5, r6, space=20, title=True, format=1, head="EMPLOYEES OF KRUSTY KRAB",
            foot=f"TOTAL SALARY: {1500 + 1000 + 1500 + 2000 + 3000 + 12000}", nullentity="--UNKNOWN--")