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
  perma_title = document.getElementById('perma-title');
  cta_btn = document.getElementById('cta-btn');
  prof_pic = document.getElementById('prof-pic');
  // new_quote_btn = document.getElementById('new-quote-btn');

  if (pageName == 'alice') {
    perma_title.classList.add("alice-title");
    perma_title.classList.remove("potter-title");
    perma_title.innerHTML = 'We\'Re aLL mAd HeRe';

    cta_btn.classList.add('alice-btn');
    cta_btn.classList.remove('potter-btn');
    cta_btn.innerHTML = 'Go Down the Rabbit-Hole';
    cta_btn.setAttribute( "onClick", "updateSentence(\"/\");");

    prof_pic.src = '/static/img/cheshire-face.png';
    // new_quote_btn.href = "/";

    // GET: new alice sentence
    updateSentence("/");
  }

  else if (pageName == 'potter') {
    perma_title.classList.add("potter-title");
    perma_title.classList.remove("alice-title");
    perma_title.innerHTML = 'I solemnly swear I\'m Up to No Good';

    cta_btn.classList.add('potter-btn');
    cta_btn.classList.remove('alice-btn');
    cta_btn.innerHTML = 'Reveal Your Secrets';
    cta_btn.setAttribute( "onClick", "updateSentence(\"/potter\");");

    prof_pic.src = '/static/img/hp-face.png';
    // new_quote_btn.href = "/potter";

    // GET: new potter sentence
    updateSentence("/potter");
  }
}

function updateSentence(url_route) {
  $.get(url_route, function( data ) {
    let new_sentence_parent_div = $("#markov-sentence", $(data))
    let new_sentence = new_sentence_parent_div[0].innerHTML
    markov_sentence = document.getElementById('markov-sentence');
    markov_sentence.innerHTML = new_sentence;
  });
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
