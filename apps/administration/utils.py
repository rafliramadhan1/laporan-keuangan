from apps.administration.models import Administration


def get_all_administration_data(username):
    tipe = [
        "pemasukan",
        "pengeluaran"
    ]
    data = {}
    for n in range(len(tipe)):
        for nominal in Administration.objects.filter(username=username, tipe=tipe[n]):
            data[nominal.id] = {}
            data[nominal.id]["month"] = Administration.objects.get(id=nominal.id).created_at.month
            data[nominal.id]["year"] = Administration.objects.get(id=nominal.id).created_at.year
    year = list(set([data[x]["year"] for x in [n for n in data.keys()]]))
    administration_year = [year[x] for x in range(len(year))]
    month = list(set([data[x]["month"] for x in data.keys()]))
    year_month = {}
    for j in range(len(administration_year)):
        ym = []
        for x in data.keys():
            if data[x]["year"] == administration_year[j]:
                ym.append(x)
            year_month[administration_year[j]] = ym
    year_month_id = {}
    for j in range(len(administration_year)):
        for x in range(len(month)):
            ymi = []
            for b in range(len(year_month[administration_year[j]])):
                a = Administration.objects.get(id=year_month[administration_year[j]][b])
                ymi.append({a.created_at.month: a.id})
            year_month_id[administration_year[j]] = ymi
    year_month_set = {}
    for x in year_month_id.keys():
        yms = []
        for s in range(len(year_month_id[x])):
            for c in year_month_id[x][s].keys():
                yms.append(c)
            year_month_set[x] = list(set(yms))
    year_month_id_set = {}
    for x in year_month.keys():
        year_month_id_set[x] = {}
        ymi_set = year_month_set[x]
        for c in range(len(ymi_set)):
            for sa in range(len(year_month_set[x])):
                year_month_id_list = []
                for kk in [dd for dd in year_month[x]]:
                    if Administration.objects.get(id=kk).created_at.month == year_month_set[x][sa]:
                        year_month_id_list.append(kk)
                year_month_id_set[x][year_month_set[x][sa]] = year_month_id_list
    administration_data = {}
    for jj in year_month_id_set.keys():
        administration_data[jj] = {}
        for dd in [kl for kl in year_month_id_set[jj].keys()]:
            income = []
            outcome = []
            for x in year_month_id_set[jj][dd]:
                f = Administration.objects.get(id=x)
                if f.tipe == "pemasukan":
                    income.append(f.nominal)
                else:
                    outcome.append(f.nominal)
            total_income = 0
            for total in income:
                total_income += total
            total_outcome = 0
            for total in outcome:
                total_outcome += total
            administration_data[jj][dd] = {}
            administration_data[jj][dd]["income"] = total_income
            administration_data[jj][dd]["outcome"] = total_outcome
            administration_data[jj][dd]["profit"] = total_income - total_outcome
    return administration_data
