
import os

EXP_VER = "v12"

mkdir = lambda p: 0 if os.path.exists(p) else (os.makedirs(p), 1)[1]

### CLASS: DATASET STATIC INFO
class DataStaticInfo:

    VER = "*"
    SEP = "_"
    META_SEP = "-"
    EXT_SEP = "."

    BEGIN_k = "start"; END_k = "end"; LABEL_k = "label"; DUR_k = "dur"
    ANOT_HEADER = [BEGIN_k, END_k, LABEL_k]

    AGE_k = 'age'
    GENDER_k = 'gender'
    HEIGHT_k = 'height'
    WEIGHT_k = 'weight'

    ANOT_LABELS = ['cc', 'ss', 'aa', 'yy', 'ee', 'ii', 'xx', 'zz', 'uu', 'oo', 'ii-n']
    ANOT_TAG = "anot--"

    def get_anot_tag(self, tag):
        return f"{self.ANOT_TAG}{tag}"

    fkeys = {
        "APP_CODE": "app_code", # 0
        "SID":"sub_id", # 1
        "FCLASS": "file_class", # 2
        "FCIDX": "file_xindex", # 3
        "SCORE": "score", # 4
        "FFMT": "file_format", # 5
        "FNAME": "file_name", # 6
        "FPATH": "file_path", # 7
        "FMATCH": "file_match" # 8
    }