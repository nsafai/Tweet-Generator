function openPage(pageName, color) {

  // CHANGE BODY COLOR BASED ON WHAT TAB WAS JUST CLICKED
  document.body.style.backgroundColor = color;

  // UPDATE CONTENT AND STYLING
  perma_title = document.getElementById('perma-title');
  cta_btn = document.getElementById('cta-btn');
  prof_pic = document.getElementById('prof-pic');
  markov_sentence = document.getElementById('markov-sentence');

  if (pageName == 'alice') {
    perma_title.classList.add("alice-title");
    perma_title.classList.remove("potter-title");
    perma_title.classList.remove("bride-title");
    perma_title.innerHTML = 'We\'Re aLL mAd HeRe';

    cta_btn.classList.add('alice-btn');
    cta_btn.classList.remove('potter-btn');
    cta_btn.classList.remove('bride-btn');
    cta_btn.innerHTML = 'Go Down the Rabbit-Hole';
    cta_btn.setAttribute( "onClick", "updateSentence(\"/\");");

    prof_pic.src = '/static/img/cheshire-face.png';

    // clear sentence
    markov_sentence.innerHTML = ''
    // GET: new alice sentence
    updateSentence("/");
  }

  else if (pageName == 'potter') {
    perma_title.classList.add("potter-title");
    perma_title.classList.remove("alice-title");
    perma_title.classList.remove("bride-title");
    perma_title.innerHTML = 'I Solemnly Swear I\'m Up to No Good';

    cta_btn.classList.add('potter-btn');
    cta_btn.classList.remove('alice-btn');
    cta_btn.classList.remove('bride-btn');
    cta_btn.innerHTML = 'Reveal Your Secrets';
    cta_btn.setAttribute( "onClick", "updateSentence(\"/potter\");");

    prof_pic.src = '/static/img/hp-face.png';

    // clear sentence
    markov_sentence.innerHTML = ''
    // GET: new potter sentence
    updateSentence("/potter");
  }

  else if (pageName == 'bride') {
    perma_title.classList.add("bride-title");
    perma_title.classList.remove("alice-title");
    perma_title.classList.remove("potter-title");
    perma_title.innerHTML = 'Mawage is wot bwings us togeder tooday.';

    cta_btn.classList.add('bride-btn');
    cta_btn.classList.remove('potter-btn');
    cta_btn.classList.remove('alice-btn');
    cta_btn.innerHTML = 'As you wish';
    cta_btn.setAttribute( "onClick", "updateSentence(\"/bride\");");

    prof_pic.src = '/static/img/pb-face.png';

    // clear sentence
    markov_sentence.innerHTML = ''
    // GET: new princess of the bride sentence
    updateSentence("/bride");
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

// set the correct tab to default
default_tab_theme = document.getElementById('theme-tab-name').innerHTML;
// there is only 1 correct tab, but getElementsByClass always returns an array
matching_tabs = document.getElementsByClassName(default_tab_theme);
// there is only 1 result, so grab first result of array
correct_tab = matching_tabs[0];
// add unique id to correct tab so we can tell JS to open it
correct_tab.setAttribute("id", "defaultOpen");
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
