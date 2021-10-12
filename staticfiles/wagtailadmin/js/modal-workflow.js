!function(){"use strict";var o,t={70533:function(o,t,e){var n=this&&this.__importDefault||function(o){return o&&o.__esModule?o:{default:o}};t.__esModule=!0;var r=n(e(73609));window.ModalWorkflow=function(o){var t={},e=o.responses||{},n=o.onError||function(){};r.default("body > .modal").remove();var a=r.default('<div class="modal fade" tabindex="-1" role="dialog" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <button type="button" class="button close button--icon text-replace" data-dismiss="modal"><svg class="icon icon-cross" aria-hidden="true" focusable="false"><use href="#icon-cross"></use></svg>'+wagtailConfig.STRINGS.CLOSE+'</button>\n      <div class="modal-body"></div>\n    </div>\x3c!-- /.modal-content --\x3e\n  </div>\x3c!-- /.modal-dialog --\x3e\n</div>');return r.default("body").append(a),a.modal("hide"),t.body=a.find(".modal-body"),t.loadUrl=function(o,e){r.default.get(o,e,t.loadResponseText,"text").fail(n)},t.postForm=function(o,e){r.default.post(o,e,t.loadResponseText,"text").fail(n)},t.ajaxifyForm=function(o){r.default(o).each((function(){var o=this.action;"get"===this.method.toLowerCase()?r.default(this).on("submit",(function(){return t.loadUrl(o,r.default(this).serialize()),!1})):r.default(this).on("submit",(function(){return t.postForm(o,r.default(this).serialize()),!1}))}))},t.loadResponseText=function(o){var e=JSON.parse(o);t.loadBody(e)},t.loadBody=function(e){e.html&&(t.body.html(e.html),a.modal("show")),o.onload&&e.step&&e.step in o.onload&&o.onload[e.step](t,e)},t.respond=function(o){if(o in e){var n=Array.prototype.slice.call(arguments,1);e[o].apply(t,n)}},t.close=function(){a.modal("hide")},t.loadUrl(o.url,o.urlParams),t}},73609:function(o){o.exports=jQuery}},e={};function n(o){var r=e[o];if(void 0!==r)return r.exports;var a=e[o]={id:o,loaded:!1,exports:{}};return t[o].call(a.exports,a,a.exports,n),a.loaded=!0,a.exports}n.m=t,o=[],n.O=function(t,e,r,a){if(!e){var i=1/0;for(u=0;u<o.length;u++){e=o[u][0],r=o[u][1],a=o[u][2];for(var l=!0,d=0;d<e.length;d++)(!1&a||i>=a)&&Object.keys(n.O).every((function(o){return n.O[o](e[d])}))?e.splice(d--,1):(l=!1,a<i&&(i=a));l&&(o.splice(u--,1),t=r())}return t}a=a||0;for(var u=o.length;u>0&&o[u-1][2]>a;u--)o[u]=o[u-1];o[u]=[e,r,a]},n.n=function(o){var t=o&&o.__esModule?function(){return o.default}:function(){return o};return n.d(t,{a:t}),t},n.d=function(o,t){for(var e in t)n.o(t,e)&&!n.o(o,e)&&Object.defineProperty(o,e,{enumerable:!0,get:t[e]})},n.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(o){if("object"==typeof window)return window}}(),n.hmd=function(o){return(o=Object.create(o)).children||(o.children=[]),Object.defineProperty(o,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+o.id)}}),o},n.o=function(o,t){return Object.prototype.hasOwnProperty.call(o,t)},n.r=function(o){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(o,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(o,"__esModule",{value:!0})},n.j=922,function(){var o={922:0};n.O.j=function(t){return 0===o[t]};var t=function(t,e){var r,a,i=e[0],l=e[1],d=e[2],u=0;for(r in l)n.o(l,r)&&(n.m[r]=l[r]);if(d)var s=d(n);for(t&&t(e);u<i.length;u++)a=i[u],n.o(o,a)&&o[a]&&o[a][0](),o[i[u]]=0;return n.O(s)},e=self.webpackChunkwagtail=self.webpackChunkwagtail||[];e.forEach(t.bind(null,0)),e.push=t.bind(null,e.push.bind(e))}(),n.O(void 0,[751],(function(){return n(70533)}));var r=n.O(void 0,[751],(function(){return n(90971)}));r=n.O(r)}();
//# sourceMappingURL=modal-workflow.js.map