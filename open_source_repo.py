# 20211961 open_source_repo
# git

import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

# 선택한 날짜의 메모를 표시하는 함수
def on_date_select(event):
    # 선택된 날짜를 가져온다.
    selected_date = cal.selection_get()
    
    # 해당 날짜에 대한 메모를 텍스트 입력 필드에 표시한다.
    memo_entry.delete(1.0, tk.END)
    memo_entry.insert(tk.END, memos.get(selected_date, ""))

# 메모를 저장하는 함수
def save_memo():
    # 선택한 날짜에 메모를 저장한다. 
    selected_date = cal.selection_get()
    memos[selected_date] = memo_entry.get(1.0, tk.END).strip()
    print(f"날짜: {selected_date}, 메모: {memos[selected_date]}")

# 메모를 검색하는 함수
def search_memo():
    # 사용자의 검색어를 가져온다.
    search_query = search_entry.get()
    if not search_query:
        messagebox.showinfo("검색", "검색어를 입력해주세요.")
        return
	# 사용자의 입력과 기존에 입력된 메모와 일치하는 것을 검색한다. 
    matching_memos = []
    for date, memo in memos.items():
        if search_query.lower() in memo.lower():
            matching_memos.append(f"{date}: {memo}")

	# 검색 결과를 출력한다. 
    if matching_memos:
        result_message = "\n\n".join(matching_memos)
        messagebox.showinfo("검색 결과", f"일치하는 메모를 찾았습니다.:\n\n{result_message}")
    else:
        messagebox.showinfo("검색 결과", "일치하는 메모가 없습니다.")

# tkinker를 이용한 gui 프로그램 창을 생성한다.
root = tk.Tk()
root.title("한국어 달력")

# 메모를 저장할 딕셔너리를 초기화한다.
memos = {}

# 사용자 정의 폰트를  설정한다.
custom_font = ('Arial', 12, 'bold')

# 캘린더 위젯을  생성하고  스타일을  설정한다.
cal = Calendar(root, selectmode='day', font=custom_font,
               background='white', foreground='black', bordercolor='gray',
               headersbackground='#6096B4', headersforeground='white',
               selectbackground='#27374D', selectforeground='white',
               normalbackground='white', normalforeground='black',
               weekendbackground='#BDDCD6', weekendforeground='black',
               othermonthforeground='gray50', othermonthbackground='white',
               othermonthwebackground='#EEE9DA')

cal.pack(pady=20)
cal.bind("<<CalendarSelected>>", on_date_select)

# 메모 입력을 위한 텍스트 필드를 구현한다.
memo_entry = tk.Text(root, height=5, width=50)
memo_entry.pack(pady=5)

# 메모 저장 버튼을 구현한다. 
save_button = tk.Button(root, text="메모 저장", command=save_memo)
save_button.pack(pady=5)

# 검색 필드 및 버튼을 구현한다. 
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="메모 검색", command=search_memo)
search_button.pack(pady=5)

# gui 프로그램을 실행한다. 
root.mainloop()

