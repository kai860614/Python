def ten_divided_by(num):
    try:
    # 試圖執行可能引發異常的程式碼
        result = 10 / num  # 這個有機會引發 除以 0 的異常

    except ZeroDivisionError:
    # 處理特定類型的異常
        print("ZeroDivisionError occured.")

    else:
    # 當沒有異常時執行
        print(f"No Exception. The result is {result}")

    finally:
    # 無論是否發生異常都要執行
        print("--- Finally Finished ---")


ten_divided_by(0)
ten_divided_by(10)
