window.addEventListener("load", function () {
	hideAll();
	inViewCheck();
	window.addEventListener("scroll", function () {
		inViewCheck();
	});
});

function hideAll() {
	document.querySelectorAll('.animated').forEach(targetObj => {
		if ((!document.body.classList.contains('mobile-device-nuts')) || (document.body.classList.contains('mobile-device-nuts') && window.innerWidth > 767)) {
			var targetRect = targetObj.getBoundingClientRect();
			var targetObjX = targetRect.top + (targetObj.offsetHeight / 3);
			if (targetObjX > window.innerHeight) {
				targetObj.classList.remove("animated");
				targetObj.classList.add("hideMe");
			}
		}
	});
};

function inViewCheck() {
	const hiddenItems = [].slice.call(document.querySelectorAll('.hideMe'), 0).reverse();
	hiddenItems.forEach(targetObj => {
		var targetRect = targetObj.getBoundingClientRect();
		var offsetTop = (targetRect.top + window.scrollY);
		var a = offsetTop + targetObj.offsetHeight;
		var b = window.pageYOffset + window.innerHeight;
		if (targetObj.offsetHeight > window.innerHeight) {
			a = offsetTop
		}
		if (a < b) {
			var objectClass = targetObj.className.replace('hideMe', 'animated');
			targetObj.style.visibility = "hidden";
			targetObj.removeAttribute("class");
			setTimeout(function () {
				targetObj.style.visibility = "visible";
				targetObj.setAttribute('class', objectClass);
			}, 0.01);
			var animEvents = ["webkitAnimationEnd", "mozAnimationEnd", "oAnimationEnd", "animationEnd"];
			animEvents.forEach(function (e) {
				window.addEventListener(e, function (event) {
					targetObj.classList.remove(targetObj.getAttribute("data-appear-anim-style"));
				});
			});
		}
	});
};

window.requestAnimFrame = (function () {
	return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || function (callback) {
		window.setTimeout(callback, 1000 / 60);
	};
})();