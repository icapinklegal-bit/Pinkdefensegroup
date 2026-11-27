(function(){
  // mobile menu
  var btn=document.querySelector('.menu-btn'),nav=document.getElementById('nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false');});}
  // testimonial rotator
  document.querySelectorAll('.quotes').forEach(function(box){
    var qs=box.querySelectorAll('.quote'),dots=box.querySelector('.qdots');if(!qs.length||!dots)return;
    var i=0,t;
    function show(n){qs[i].classList.remove('on');dots.children[i].classList.remove('on');i=(n+qs.length)%qs.length;qs[i].classList.add('on');dots.children[i].classList.add('on');}
    qs.forEach(function(_,n){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Show review '+(n+1));b.addEventListener('click',function(){show(n);clearInterval(t);});dots.appendChild(b);});
    qs[0].classList.add('on');dots.children[0].classList.add('on');
    t=setInterval(function(){show(i+1);},7000);
  });
  // attorney photos: local file -> remote fallback -> monogram
  document.querySelectorAll('img[data-fallback]').forEach(function(img){
    function fail(){var f=img.getAttribute('data-fallback');if(f){img.removeAttribute('data-fallback');img.src=f;}else{img.style.display='none';}}
    img.addEventListener('error',fail);
    if(img.complete&&img.naturalWidth===0)fail();
  });
  // form: stamp source page
  document.querySelectorAll('form.form').forEach(function(f){var p=f.querySelector('input[name=page]');if(p)p.value=location.href;});
})();
