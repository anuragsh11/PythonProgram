def replacechar(s):
    chr={"<":"&lt; ",">":"&gt; ","&":"&amp; "}
    finalStr=""
    for i in s:
        if i in chr:
            finalStr+=chr[i]
        else:
            finalStr+=i
    return finalStr



str ="Hello <World> Goodbye & World"
print(replacechar(str))