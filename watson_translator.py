# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:32:32 2018

@author: IstukiHamano
"""

import json
from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud import WatsonApiException


texts=['今日は晴れです','明日も雨です','最近はやりのEDM','私の名前はジャスティンビーバーです','あなたの名前はマーティンギャリックスです!']
#api使うためのユーザ認証情報セット
language_translator=LanguageTranslatorV3(
        version='2018-10-27',
        iam_apikey='Wwf5mwrlsNETHg4ij0jSDB9kQ-SOfJzpjWjfGyl7oLrj',
        url='https://gateway.watsonplatform.net/language-translator/api'
        )

#エラー処理（apiが正常に呼び出せたか、HTTP応答コードを表示）
#例外で投げられるのはWatsonApiException
#200番：成功、400番：なんらかの失敗、500番：内部システムエラー
try:
    #Invoke a Language Translator method(メソッド実行)
    #translation=language_translator.translate(text='こんにちわ',model_id='jp-en').get_result()
    
    #翻訳を行う
    translation=language_translator.translate(
            texts,
            model_id='ja-en').get_result()
    print(json.dumps(translation,indent=2,ensure_ascii=False))
    
    #入力された言語が何か判定
    languages=language_translator.identify('私の名前はジャスティンビーバーです').get_result()
    print(json.dumps(languages, indent=2))
    
    #識別可能な言語一覧を表示する
    #languages=language_translator.list_identifiable_languages().get_result()
    #print("識別可能な言語一覧表示"+json.dumps(languages,indent=2))    
    
    #利用可能モデル一覧表示
    #models=language_translator.list_models().get_result()
    #print(json.dumps(models,indent=2))
    
    
except WatsonApiException as ex:
    print("api呼び出し失敗：エラーコード"+str(ex.code)+":エラーメッセージ"+ex.message)

  
#watsonapiでリクエストで送るデータにヘッダー情報も設定できる
#リクエストで解析するデータはIBMチームに収集されているが、そうしない設定もできる
#データ収集されたくなければx-watson-learning-opt-outをfalseか0以外の値に設定
#language_translator.set_default_headers({'x-watson-learning-opt-out':"true"})


#メソッドからの戻り値はDetailedResponseオブジェクト
#print("HTTP response statusを表示:"+translation.get_status_code())
#print(json.dump(translation,indent=2,ensure_ascii=False))
#print("responseのヘッダー表示:"+translation.get_headers())

