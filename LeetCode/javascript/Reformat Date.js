const month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];


var reformatDate = function(date) 
{
    let split = date.split(" ");

    let day = parseInt(split[0]);
    let mt = month.indexOf(split[1]) + 1;

    return `${split[2]}-${mt < 10? "0" : ""}${mt}-${day < 10? "0" : ""}${day}` ;
};