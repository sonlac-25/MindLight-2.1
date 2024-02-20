//W3 Schools localStorage function: https://www.w3schools.com/jsref/prop_win_localstorage.asp
//Used in name and history function
function findBoth (petsId, cuteId){
    
    findPhoto (petsId);
    findPhoto (cuteId)
    //Calls same function for both images (passes ids for image 1 and 2)
}


function findPhoto(id) {
    var num = parseInt (27 * Math.random() +1);
    //Takes a random number for one of the 27 photos in each photo folder
    var image = document.getElementById(id);
    //Calls the image and sets a variable equal to the image
    var img = id + "/" + id + num + ".jpg"
    //calls from folder w id name (i.e. Pets/Pets + the random number that had been generated)
    image.src = img
    //Calls the image source and sets it equal to the created source to set the new image
}
  
  function checkStorage() {
    var user = localStorage.getItem("name");
    //Calls items if it exists
    if (user != null && user!="") {
        //If it had existed or had not been cleared
      alert("Hello again " + user + "!");
        //Welcomes person with previously entered username
    } else {
       user = prompt("Please enter your name:","");
       //If the user had not existed or had been cleared, it generates a prompt and sets the variable user equal to whatever the person answers
       if (user != "" && user != null) {
        //If the person actually entered something (did not cancel or enter an empmty string)
        localStorage.setItem("name",user);
        //Sets category "name" to call what they entered
        let x = localStorage.getItem("name");
        //Calls item
         alert("Hello " + x + "!");
        //Says hello to person
       }
    }
    
        //console.log(localStorage.getItem("entry"))
    
       
        //console.log("functioning")
}
function checkStorageHistory() {
    //Called if user enters the history page
    document.getElementById("historyEntries").innerHTML = localStorage.getItem("entry");
    //Calls the "entry" category from the local storage and sets the HTML of the history section equal to this specific function

    //All other code is the same as the checkStorage() function
    var user = localStorage.getItem("name");
    if (user != null && user!="") {
      alert("Hello again " + user + "!");
    } else {
       user = prompt("Please enter your name:","");
       if (user != "" && user != null) {
        localStorage.setItem("name",user);
        let x = localStorage.getItem("name");
         alert("Hello " + x + "!");
       }
    }
    
        //console.log(localStorage.getItem("entry"))
            //Previous console tests that can be used to check functionality
        //console.log("functioning")
}

  function clearStorage() {
    localStorage.setItem("name","");
    //Sets "name" to empty string (basically deleting the category)
  }

  function addToHistory (color) {
    //user passes associated color of event
    const date = new Date();
    //Calls date and time and sets it equal to an array
    var input1 = document.getElementById("feelings").value
    //Calls input from the textarea with id "feelings"
    var input2 = document.getElementById("future").value
    //Calls input from the textarea with id "future"
    var inputData = date + "<br/>" + color + " entry" + "<br/>" + input1 + "<br/>" + input2;
    //Creates variable that is the date + the color the user associated with the event + the first input + the second input
    if (localStorage.getItem("entry") != "" && localStorage.getItem("entry") != null){
        //Basically, if the input is not empty
        var newInput = "<br/>" +inputData + "<br/><br/><br/>" +  localStorage.getItem("entry")+ "<br/>";
        //creates variable that adds this specific entry to all other entries
        localStorage.setItem("entry", newInput)
        //Sets category of entry 
    } else {
        localStorage.setItem("entry", inputData)
        //If there was nothing stored, code just adds the entry to the history
    }
    
  }


  function clearHistory () {
    localStorage.setItem("entry", "")
    //Clears history category
    document.getElementById("historyEntries").innerHTML=""
    //Physically clears history from page
  }
