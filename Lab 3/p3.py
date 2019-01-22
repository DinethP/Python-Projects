import pickle


def load_data(file):
    try:
        file_obj = open(file, "rb")
        dic = pickle.load(file_obj)
        return dic
    except Exception:
        return {}


def query(prof_name):
    dic = load_data("dept-prof.pydata")
    return [department for department in dic if prof_name in dic[department]]


def update():
    dic = load_data("dept-prof.pydata")
    dic.pop("Artificial Intelligence")  
    dic['Space Engineering'] = ['Musk', 'Andy', 'Jane']
    pickle.dump(dic, open("dept-prof-updated.pydata", "wb"))


def get_depts_size():
    dic = load_data("dept-prof-updated.pydata")
    for department in dic:
        dic[department] = len(dic[department])
    return dic
