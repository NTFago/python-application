def is_ap(nums, length):
    """input: nums (type:list, description:a list of numbers)
              length (type:int, description:the length of the nums)
       output:result (type:str, description:the type of the number list)
       优先级：常数列 > 等差数列 = 等比数列(即一个数列同时为常数列和等差数列时，先返回常数列)
       当一个数列的公差为0时，这个数列为常数列且公比为1
       当一个数列的项数大于2时，若这个数列既为等比数列又是等差数列时，则这个数列为常数列
    """
    if length == 0:
        return "数列不存在"
    elif length == 1:
        return "常数列"
    elif length == 2:
        return "常数列" if nums[0] == nums[1] else "既是等差数列，又是等比数列"
    else:
        alld, allq = [], []
        for i in range(length - 1):     # 循环 length - 1 次，遍历到倒数第二项过
            d = nums[i + 1] - nums[i]
            q = nums[i + 1] / nums[i]
            alld.append(d)
            allq.append(q)
        print(alld, allq)
        if alld.count(0) == length - 1: # d和q与数列长度为 length - 1个d和q
            return "常数列"
        elif alld.count(d) == length - 1:
            return "等差数列"
        elif allq.count(q) == length - 1:
            return "等比数列"
        else:
            return "其他数列"

if __name__ == "__main__":
    try:
        ln = list(input("请输入一个数列（各数字间用','隔开）：").replace(" ", "").replace("，", "").replace(",",""))
        # replace语句为可能出现的输入错误处理
        ls = list(map(float, ln))
        result = is_ap(ls, len(ls))
        print(result)
    except Exception as error:
        import traceback    # python内置库，输出详细的错误信息
        print("出现错误：", error)
        print("以下是详细的错误信息：\n", traceback.format_exc())
