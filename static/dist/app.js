!function(){"use strict";var a=document.querySelector(".toggle-night"),b=document.body.classList,c=document.querySelector(".ground"),d=function(){a.innerHTML='<span class="fa fa-moon-o"></span>',b.remove("night"),b.add("day"),c.src="/static/images/ground.svg"},e=function(){a.innerHTML='<span class="fa fa-sun-o"></span>',b.remove("day"),b.add("night"),c.src="/static/images/ground-night.svg"};a.onclick=function(){document.body.classList.contains("night")?d():e()},d()}();
//# sourceMappingURL=app.js.map