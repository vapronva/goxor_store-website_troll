function hideAll() {
	document.querySelectorAll('.animated').forEach(targetObj => {
		let targetRect = targetObj.getBoundingClientRect();
		let targetObjX = targetRect.top + (targetObj.offsetHeight / 3);
		if ((!document.body.classList.contains('mobile-device-nuts')) || (document.body.classList.contains('mobile-device-nuts') && window.innerWidth > 767)) {
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
		let targetRect = targetObj.getBoundingClientRect();
		let offsetTop = (targetRect.top + window.scrollY);
		let a = offsetTop + targetObj.offsetHeight;
		let b = window.pageYOffset + window.innerHeight;
		let animEvents = ["webkitAnimationEnd", "mozAnimationEnd", "oAnimationEnd", "animationEnd"];
		let objectClass = targetObj.className.replace('hideMe', 'animated');
		if (targetObj.offsetHeight > window.innerHeight) {
			a = offsetTop
		}
		if (a < b) {
			targetObj.style.visibility = "hidden";
			targetObj.removeAttribute("class");
			setTimeout(function () {
				targetObj.style.visibility = "visible";
				targetObj.setAttribute('class', objectClass);
			}, 0.01);
			animEvents.forEach((e) => {
				window.addEventListener(e, (_) => {
					targetObj.classList.remove(targetObj.getAttribute("data-appear-anim-style"));
				});
			});
		}
	});
};

window.addEventListener("load", () => {
	hideAll();
	inViewCheck();
	window.addEventListener("scroll", () => {
		inViewCheck();
	});
});

window.requestAnimFrame = (() => {
	return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || function (callback) {
		window.setTimeout(callback, 1000 / 60);
	};
})();