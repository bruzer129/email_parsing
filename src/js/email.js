     function readFile() {
       var fileTxt, fileName, fileList, fileReader
       var txtArea = document.getElementById("txtArea")
       var keys = ['To', 'From', 'Subject', 'Date']
       // regex's are the same but this gives flexibility.
       var regex = [
         `\s*(${keys[0]}: .*)[\r\n]`,
         `\s*(${keys[1]}: .*)[\r\n]`,
         `\s*(${keys[2]}: .*)[\r\n]`,
         `\s*(${keys[3]}: .*)[\r\n]`
       ]

       fileList = document.getElementById("fileToRead")
       fileReader = new FileReader();
       fileName = fileList.files[0]
       fileReader.onload = function(evt) {
         fileTxt = fileReader.result
         txtArea.innerHTML = fileTxt

         var tdCell
         var res
         var val
         keys.forEach(function(item, idx) {
           res = fileTxt.match(regex[idx])
           val = keys[idx]
           // html id's have to be named the same as item
           tdCell = document.getElementById(item)
           if (res !== null)  {
             var strVal = res[1].replace(/</g, '&lt;')
             tdCell.innerHTML = strVal
             console.log('match key: ' + val + ': ' + strVal)
           } else {
             tdCell.innerHTML = val
           }
         })
       };

       fileReader.onerror = function(evt) {
           var errDiv = document.getElementById("errDiv")
           errDiv.innerHTML = 'ERROR reading the file!'
         console.log('Error reading file: ' + evt.target)
       };
       console.log('Initial readyState: ' + fileReader.readyState)
       fileReader.readAsText(fileName, "UTF-8");

     }
