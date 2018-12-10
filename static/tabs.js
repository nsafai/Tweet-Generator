function openPage(pageName, elmnt, color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById("tab-content").style.display = "block";
  elmnt.style.backgroundColor = color;
  document.body.style.backgroundColor = color;

  // UPDATE CONTENT AND STYLING
  permatitle = document.getElementById('perma-title');
  ctabtn = document.getElementById('cta-btn');
  profpic = document.getElementById('prof-pic');

  if (pageName == 'alice') {
    permatitle.classList.add("alice-title");
    permatitle.classList.remove("potter-title");
    permatitle.innerHTML = 'We\'Re aLL mAd HeRe';

    ctabtn.classList.add('alice-btn');
    ctabtn.classList.remove('potter-btn');
    ctabtn.innerHTML = 'Go Down the Rabbit-Hole';

    profpic.src = '/static/img/cheshire-face.png';

  } else if (pageName == 'potter') {
    permatitle.classList.add("potter-title");
    permatitle.classList.remove("alice-title");
    permatitle.innerHTML = 'I solemnly swear I\'m Up to No Good';

    ctabtn.classList.add('potter-btn');
    ctabtn.classList.remove('alice-btn');
    ctabtn.innerHTML = 'Reveal Your Secrets';

    profpic.src = '/static/img/hp-face.png';
  }
}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
