import pandas as pd
import ntpath

def text_preprocessing(path):
    filename = ntpath.basename(path)
    df = pd.read_csv(path)
    df.insert(6, "Audio_class", '', True)

    def replace(origin, modified):
        if not pd.isna(modified):
            modified = modified.replace("#", " ")
            modified = modified.replace("\n", "")
            new_class_list = modified.split()
            return "、".join(new_class_list)
        else:
            return origin

    df['Audio_class'] = df.apply(lambda x: replace(x['Audio_content_Yamnet'], x['Audio_content_User']), axis=1)
    df.to_csv('new_'+filename, index = False)
    return 'new_'+filename