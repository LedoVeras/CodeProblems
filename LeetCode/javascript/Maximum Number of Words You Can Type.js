var canBeTypedWords = function(text, brokenLetters) 
{
    let splited = text.split(" ");
    let letters = brokenLetters.split("");
    let canWrite = splited.length;

    for (let i = 0; i < splited.length; i++)
    {
        let curWord = splited[i];
        for (let j = 0; j < letters.length; j++)
        {
            if(curWord.includes(letters[j]))
            {
                canWrite --;
                break;
            }
        }
    }

    return canWrite;
};