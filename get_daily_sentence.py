import requests
import os
import datetime

def main():
    try:
        # 获取金山词霸每日一句
        response = requests.get("http://open.iciba.com/dsapi/")
        data = response.json()
        
        print(f"API响应: {data}")
        
        # 获取所需字段
        content = data.get('content', '')
        note = data.get('note', '')
        translation = data.get('translation', '')
        picture = data.get('picture2', '')
        date = data.get('dateline', datetime.date.today().strftime('%Y-%m-%d'))
        
        # 处理翻译字段（去除"小编的话："）
        if '小编的话：' in translation:
            translation = translation.split('小编的话：')[1].strip()
        
        # 将数据写入文件
        for filename, content in [
            ('content.txt', content),
            ('note.txt', note),
            ('translation.txt', translation),
            ('picture_url.txt', picture),
            ('date.txt', date)
        ]:
            with open(filename, 'w') as f:
                f.write(content)
                
    except Exception as e:
        print(f"错误: {e}")
        # 使用默认值作为回退
        fallback_date = datetime.date.today().strftime('%Y-%m-%d')
        for filename, content in [
            ('content.txt', 'Something went wrong'),
            ('note.txt', '请稍后再试'),
            ('translation.txt', 'API请求失败'),
            ('picture_url.txt', 'https://placehold.co/600x400?text=图片加载失败'),
            ('date.txt', fallback_date)
        ]:
            with open(filename, 'w') as f:
                f.write(content)

if __name__ == '__main__':
    main()
