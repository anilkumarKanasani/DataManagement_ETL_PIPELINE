import pandas as pd 


input_files_location = 'D:/DataManagement-2/DS4C_DataSet_pandas_checking/'

# Standard List of Proviences gathered from Regions CSV
provience_codes = {'Seoul' : 10000,
                'Busan' : 11000,
                'Daegu' : 12000,
                'Incheon': 14000, 
                'Gwangju': 13000, 
                'Daejeon' : 15000,
                'Ulsan' : 16000, 
                'Sejong' : 17000,
                'Gyeonggi-do' : 20000 ,
                'Gangwon-do' : 30000, 
                'Chungcheongbuk-do' : 40000,
                'Chungcheongnam-do' : 41000,
                'Jeollabuk-do' : 50000,
                'Jeollanam-do' : 51000, 
                'Gyeongsangbuk-do' : 60000, 
                'Gyeongsangnam-do' : 61000,
                'Jeju-do' : 70000 }

# Standard List of Cities gathered from Regions CSV
list_of_cities = ['Seoul', 'Gangnam-gu', 'Gangdong-gu', 'Gangbuk-gu', 'Gangseo-gu', 'Gwanak-gu', 'Gwangjin-gu', 'Guro-gu', 'Geumcheon-gu', 'Nowon-gu', 'Dobong-gu', 'Dongdaemun-gu', 'Dongjak-gu', 'Mapo-gu', 'Seodaemun-gu', 'Seocho-gu', 'Seongdong-gu', 'Seongbuk-gu', 'Songpa-gu', 'Yangcheon-gu', 'Yeongdeungpo-gu', 'Yongsan-gu', 'Eunpyeong-gu', 'Jongno-gu', 'Jung-gu', 'Jungnang-gu', 'Busan', 'Geumjeong-gu', 'Gijang-gun', 'Nam-gu', 'Dong-gu', 'Dongnae-gu', 'Busanjin-gu', 'Buk-gu', 'Sasang-gu', 'Saha-gu', 'Seo-gu', 'Suyeong-gu', 'Yeonje-gu', 'Yeongdo-gu', 'Haeundae-gu', 'Daegu', 
'Dalseo-gu', 'Dalseong-gun', 'Suseong-gu', 'Gwangju', 'Gwangsan-gu', 'Incheon', 'Ganghwa-gun', 'Gyeyang-gu', 'Michuhol-gu', 'Namdong-gu', 'Bupyeong-gu', 'Yeonsu-gu', 'Ongjin-gun', 'Daejeon', 'Daedeok-gu', 'Yuseong-gu', 'Ulsan', 'Ulju-gun', 'Sejong', 'Gyeonggi-do', 'Gapyeong-gun', 'Goyang-si', 'Gwacheon-si', 'Gwangmyeong-si', 'Gwangju-si', 'Guri-si', 'Gunpo-si', 'Gimpo-si', 'Namyangju-si', 'Dongducheon-si', 'Bucheon-si', 'Seongnam-si', 'Suwon-si', 'Siheung-si', 'Ansan-si', 'Anseong-si', 'Anyang-si', 'Yangju-si', 'Yangpyeong-gun', 'Yeoju-si', 'Yeoncheon-gun', 
'Osan-si', 'Yongin-si', 'Uiwang-si', 'Uijeongbu-si', 'Icheon-si', 'Paju-si', 'Pyeongtaek-si', 'Pocheon-si', 'Hanam-si', 'Hwaseong-si', 'Gangwon-do', 'Gangneung-si', 'Goseong-gun', 'Donghae-si', 'Samcheok-si', 'Sokcho-si', 'Yanggu-gun', 'Yangyang-gun', 'Yeongwol-gun', 'Wonju-si', 'Inje-gun', 'Jeongseon-gun', 'Cheorwon-gun', 'Chuncheon-si', 'Taebaek-si', 'Pyeongchang-gun', 'Hongcheon-gun', 'Hwacheon-gun', 'Hoengseong-gun', 'Chungcheongbuk-do', 'Goesan-gun', 'Danyang-gun', 'Boeun-gun', 'Yeongdong-gun', 'Okcheon-gun', 'Eumseong-gun', 'Jecheon-si', 'Jeungpyeong-gun', 'Jincheon-gun', 'Cheongju-si', 'Chungju-si', 'Chungcheongnam-do', 'Gyeryong-si', 'Gongju-si', 'Geumsan-gun', 'Nonsan-si', 'Dangjin-si', 
'Boryeong-si', 'Buyeo-gun', 'Seosan-si', 'Seocheon-gun', 'Asan-si', 'Yesan-gun', 'Cheonan-si', 'Cheongyang-gun', 'Taean-gun', 'Hongseong-gun', 'Jeollabuk-do', 'Gochang-gun', 'Gunsan-si', 'Gimje-si', 'Namwon-si', 'Muju-gun', 'Buan-gun', 'Sunchang-gun', 'Wanju-gun', 'Iksan-si', 'Imsil-gun', 'Jangsu-gun', 'Jeonju-si', 'Jeongeup-si', 'Jinan-gun', 'Jeollanam-do', 'Gangjin-gun', 'Goheung-gun', 'Gokseong-gun', 'Gwangyang-si', 
'Gurye-gun', 'Naju-si', 'Damyang-gun', 'Mokpo-si', 'Muan-gun', 'Boseong-gun', 'Suncheon-si', 'Sinan-gun', 'Yeosu-si', 'Yeonggwang-gun', 'Yeongam-gun', 'Wando-gun', 'Jangseong-gun', 'Jangheung-gun', 'Jindo-gun', 'Hampyeong-gun', 'Haenam-gun', 'Hwasun-gun', 'Gyeongsangbuk-do', 'Gyeongsan-si', 'Gyeongju-si', 'Goryeong-gun', 'Gumi-si', 'Gunwi-gun', 'Gimcheon-si', 'Mungyeong-si', 'Bonghwa-gun', 'Sangju-si', 'Seongju-gun', 'Andong-si', 'Yeongdeok-gun', 'Yeongyang-gun', 'Yeongju-si', 'Yeongcheon-si', 'Yecheon-gun', 'Ulleung-gun', 'Uljin-gun', 'Uiseong-gun', 'Cheongdo-gun', 'Cheongsong-gun', 'Chilgok-gun', 'Pohang-si', 'Gyeongsangnam-do', 'Geoje-si', 'Geochang-gun', 'Gimhae-si', 'Namhae-gun', 'Miryang-si', 'Sacheon-si', 'Sancheong-gun', 'Yangsan-si', 'Uiryeong-gun', 'Jinju-si', 'Changnyeong-gun', 'Changwon-si', 'Tongyeong-si', 'Hadong-gun', 'Haman-gun', 'Hamyang-gun', 'Hapcheon-gun', 'Jeju-do', 'Korea']


# Standard considered accross all tables of this project
age_group_codes = {'0s' : 1,
                '10s' : 2,
                '20s' : 3,
                '30s': 4, 
                '40s': 5, 
                '50s' : 6,
                '60s' : 7, 
                '70s' : 8,
                '80s' : 9 }


# converting accumulated values into normal day wise values
def transform_accumulte(ser):
        temp= ser[0]
        ser = ser.diff()
        ser[0] = temp
        return ser

        
def transform_slices(df , col_name , value):
        # Adding slice number to male records
        df_ = df[df[col_name] == value].reset_index().drop('index', 1)
        df_['slice_no'] = pd.Series([int(i) for i in range (1 , df_.shape[0] +1 )])


        # converting accumulated values into normal day wise values
        df_["confirmed"] = transform_accumulte(df_["confirmed"] )
        df_["deceased"] = transform_accumulte(df_["deceased"] )

        if col_name == 'province':
                df_["released"] = transform_accumulte(df_["released"] )

        return df_

def replace_negative_values(ser):
        li = []
        for value in ser:
                if value >= 0 :
                        li.append(value)
                else:
                        li.append(0)
        return pd.Series(li)
