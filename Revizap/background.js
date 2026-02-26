(() => {
    var e = {
            7922(e) {
                e.exports = function(e, r) {
                    this.v = e, this.k = r
                }, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            1143(e, r, t) {
                var n = t(448);

                function a() {
                    /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/babel/babel/blob/main/packages/babel-helpers/LICENSE */
                    var r, t, o = "function" == typeof Symbol ? Symbol : {},
                        s = o.iterator || "@@iterator",
                        c = o.toStringTag || "@@toStringTag";

                    function u(e, a, o, s) {
                        var c = a && a.prototype instanceof l ? a : l,
                            u = Object.create(c.prototype);
                        return n(u, "_invoke", function(e, n, a) {
                            var o, s, c, u = 0,
                                l = a || [],
                                p = !1,
                                f = {
                                    p: 0,
                                    n: 0,
                                    v: r,
                                    a: d,
                                    f: d.bind(r, 4),
                                    d: function(e, t) {
                                        return o = e, s = 0, c = r, f.n = t, i
                                    }
                                };

                            function d(e, n) {
                                for (s = e, c = n, t = 0; !p && u && !a && t < l.length; t++) {
                                    var a, o = l[t],
                                        d = f.p,
                                        h = o[2];
                                    e > 3 ? (a = h === n) && (c = o[(s = o[4]) ? 5 : (s = 3, 3)], o[4] = o[5] = r) : o[0] <= d && ((a = e < 2 && d < o[1]) ? (s = 0, f.v = n, f.n = o[1]) : d < h && (a = e < 3 || o[0] > n || n > h) && (o[4] = e, o[5] = n, f.n = h, s = 0))
                                }
                                if (a || e > 1) return i;
                                throw p = !0, n
                            }
                            return function(a, l, h) {
                                if (u > 1) throw TypeError("Generator is already running");
                                for (p && 1 === l && d(l, h), s = l, c = h;
                                    (t = s < 2 ? r : c) || !p;) {
                                    o || (s ? s < 3 ? (s > 1 && (f.n = -1), d(s, c)) : f.n = c : f.v = c);
                                    try {
                                        if (u = 2, o) {
                                            if (s || (a = "next"), t = o[a]) {
                                                if (!(t = t.call(o, c))) throw TypeError("iterator result is not an object");
                                                if (!t.done) return t;
                                                c = t.value, s < 2 && (s = 0)
                                            } else 1 === s && (t = o.return) && t.call(o), s < 2 && (c = TypeError("The iterator does not provide a '" + a + "' method"), s = 1);
                                            o = r
                                        } else if ((t = (p = f.n < 0) ? c : e.call(n, f)) !== i) break
                                    } catch (e) {
                                        o = r, s = 1, c = e
                                    } finally {
                                        u = 1
                                    }
                                }
                                return {
                                    value: t,
                                    done: p
                                }
                            }
                        }(e, o, s), !0), u
                    }
                    var i = {};

                    function l() {}

                    function p() {}

                    function f() {}
                    t = Object.getPrototypeOf;
                    var d = [][s] ? t(t([][s]())) : (n(t = {}, s, function() {
                            return this
                        }), t),
                        h = f.prototype = l.prototype = Object.create(d);

                    function m(e) {
                        return Object.setPrototypeOf ? Object.setPrototypeOf(e, f) : (e.__proto__ = f, n(e, c, "GeneratorFunction")), e.prototype = Object.create(h), e
                    }
                    return p.prototype = f, n(h, "constructor", f), n(f, "constructor", p), p.displayName = "GeneratorFunction", n(f, c, "GeneratorFunction"), n(h), n(h, c, "Generator"), n(h, s, function() {
                        return this
                    }), n(h, "toString", function() {
                        return "[object Generator]"
                    }), (e.exports = a = function() {
                        return {
                            w: u,
                            m
                        }
                    }, e.exports.__esModule = !0, e.exports.default = e.exports)()
                }
                e.exports = a, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            2275(e, r, t) {
                var n = t(1361);
                e.exports = function(e, r, t, a, o) {
                    var s = n(e, r, t, a, o);
                    return s.next().then(function(e) {
                        return e.done ? e.value : s.next()
                    })
                }, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            1361(e, r, t) {
                var n = t(1143),
                    a = t(4273);
                e.exports = function(e, r, t, o, s) {
                    return new a(n().w(e, r, t, o), s || Promise)
                }, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            4273(e, r, t) {
                var n = t(7922),
                    a = t(448);
                e.exports = function e(r, t) {
                    function o(e, a, s, c) {
                        try {
                            var u = r[e](a),
                                i = u.value;
                            return i instanceof n ? t.resolve(i.v).then(function(e) {
                                o("next", e, s, c)
                            }, function(e) {
                                o("throw", e, s, c)
                            }) : t.resolve(i).then(function(e) {
                                u.value = e, s(u)
                            }, function(e) {
                                return o("throw", e, s, c)
                            })
                        } catch (e) {
                            c(e)
                        }
                    }
                    var s;
                    this.next || (a(e.prototype), a(e.prototype, "function" == typeof Symbol && Symbol.asyncIterator || "@asyncIterator", function() {
                        return this
                    })), a(this, "_invoke", function(e, r, n) {
                        function a() {
                            return new t(function(r, t) {
                                o(e, n, r, t)
                            })
                        }
                        return s = s ? s.then(a, a) : a()
                    }, !0)
                }, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            448(e) {
                function r(t, n, a, o) {
                    var s = Object.defineProperty;
                    try {
                        s({}, "", {})
                    } catch (t) {
                        s = 0
                    }
                    e.exports = r = function(e, t, n, a) {
                        function o(t, n) {
                            r(e, t, function(e) {
                                return this._invoke(t, n, e)
                            })
                        }
                        t ? s ? s(e, t, {
                            value: n,
                            enumerable: !a,
                            configurable: !a,
                            writable: !a
                        }) : e[t] = n : (o("next", 0), o("throw", 1), o("return", 2))
                    }, e.exports.__esModule = !0, e.exports.default = e.exports, r(t, n, a, o)
                }
                e.exports = r, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            7051(e) {
                e.exports = function(e) {
                    var r = Object(e),
                        t = [];
                    for (var n in r) t.unshift(n);
                    return function e() {
                        for (; t.length;)
                            if ((n = t.pop()) in r) return e.value = n, e.done = !1, e;
                        return e.done = !0, e
                    }
                }, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            8771(e, r, t) {
                var n = t(7922),
                    a = t(1143),
                    o = t(2275),
                    s = t(1361),
                    c = t(4273),
                    u = t(7051),
                    i = t(9);

                function l() {
                    "use strict";
                    var r = a(),
                        t = r.m(l),
                        p = (Object.getPrototypeOf ? Object.getPrototypeOf(t) : t.__proto__).constructor;

                    function f(e) {
                        var r = "function" == typeof e && e.constructor;
                        return !!r && (r === p || "GeneratorFunction" === (r.displayName || r.name))
                    }
                    var d = {
                        throw: 1,
                        return: 2,
                        break: 3,
                        continue: 3
                    };

                    function h(e) {
                        var r, t;
                        return function(n) {
                            r || (r = {
                                stop: function() {
                                    return t(n.a, 2)
                                },
                                catch: function() {
                                    return n.v
                                },
                                abrupt: function(e, r) {
                                    return t(n.a, d[e], r)
                                },
                                delegateYield: function(e, a, o) {
                                    return r.resultName = a, t(n.d, i(e), o)
                                },
                                finish: function(e) {
                                    return t(n.f, e)
                                }
                            }, t = function(e, t, a) {
                                n.p = r.prev, n.n = r.next;
                                try {
                                    return e(t, a)
                                } finally {
                                    r.next = n.n
                                }
                            }), r.resultName && (r[r.resultName] = n.v, r.resultName = void 0), r.sent = n.v, r.next = n.n;
                            try {
                                return e.call(this, r)
                            } finally {
                                n.p = r.prev, n.n = r.next
                            }
                        }
                    }
                    return (e.exports = l = function() {
                        return {
                            wrap: function(e, t, n, a) {
                                return r.w(h(e), t, n, a && a.reverse())
                            },
                            isGeneratorFunction: f,
                            mark: r.m,
                            awrap: function(e, r) {
                                return new n(e, r)
                            },
                            AsyncIterator: c,
                            async: function(e, r, t, n, a) {
                                return (f(r) ? s : o)(h(e), r, t, n, a)
                            },
                            keys: u,
                            values: i
                        }
                    }, e.exports.__esModule = !0, e.exports.default = e.exports)()
                }
                e.exports = l, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            9(e, r, t) {
                var n = t(1948).default;
                e.exports = function(e) {
                    if (null != e) {
                        var r = e["function" == typeof Symbol && Symbol.iterator || "@@iterator"],
                            t = 0;
                        if (r) return r.call(e);
                        if ("function" == typeof e.next) return e;
                        if (!isNaN(e.length)) return {
                            next: function() {
                                return e && t >= e.length && (e = void 0), {
                                    value: e && e[t++],
                                    done: !e
                                }
                            }
                        }
                    }
                    throw new TypeError(n(e) + " is not iterable")
                }, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            1948(e) {
                function r(t) {
                    return e.exports = r = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                        return typeof e
                    } : function(e) {
                        return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                    }, e.exports.__esModule = !0, e.exports.default = e.exports, r(t)
                }
                e.exports = r, e.exports.__esModule = !0, e.exports.default = e.exports
            },
            4758(e, r, t) {
                var n = t(8771)();
                e.exports = n;
                try {
                    regeneratorRuntime = n
                } catch (e) {
                    "object" == typeof globalThis ? globalThis.regeneratorRuntime = n : Function("r", "regeneratorRuntime = r")(n)
                }
            }
        },
        r = {};

    function t(n) {
        var a = r[n];
        if (void 0 !== a) return a.exports;
        var o = r[n] = {
            exports: {}
        };
        return e[n](o, o.exports, t), o.exports
    }
    t.n = e => {
        var r = e && e.__esModule ? () => e.default : () => e;
        return t.d(r, {
            a: r
        }), r
    }, t.d = (e, r) => {
        for (var n in r) t.o(r, n) && !t.o(e, n) && Object.defineProperty(e, n, {
            enumerable: !0,
            get: r[n]
        })
    }, t.o = (e, r) => Object.prototype.hasOwnProperty.call(e, r), (() => {
        "use strict";

        function e(r) {
            return e = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                return typeof e
            } : function(e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            }, e(r)
        }

        function r(r) {
            var t = function(r, t) {
                if ("object" != e(r) || !r) return r;
                var n = r[Symbol.toPrimitive];
                if (void 0 !== n) {
                    var a = n.call(r, t || "default");
                    if ("object" != e(a)) return a;
                    throw new TypeError("@@toPrimitive must return a primitive value.")
                }
                return ("string" === t ? String : Number)(r)
            }(r, "string");
            return "symbol" == e(t) ? t : t + ""
        }

        function n(e, t, n) {
            return (t = r(t)) in e ? Object.defineProperty(e, t, {
                value: n,
                enumerable: !0,
                configurable: !0,
                writable: !0
            }) : e[t] = n, e
        }

        function a(e, r, t, n, a, o, s) {
            try {
                var c = e[o](s),
                    u = c.value
            } catch (e) {
                return void t(e)
            }
            c.done ? r(u) : Promise.resolve(u).then(n, a)
        }

        function o(e) {
            return function() {
                var r = this,
                    t = arguments;
                return new Promise(function(n, o) {
                    var s = e.apply(r, t);

                    function c(e) {
                        a(s, n, o, c, u, "next", e)
                    }

                    function u(e) {
                        a(s, n, o, c, u, "throw", e)
                    }
                    c(void 0)
                })
            }
        }
        var s = t(4758),
            c = t.n(s);

        function u(e) {
            return i.apply(this, arguments)
        }

        function i() {
            return (i = o(c().mark(function e(r) {
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.abrupt("return", new Promise(function(e, t) {
                                var n = new FileReader;
                                n.onloadend = function() {
                                    return e(n.result)
                                }, n.onerror = t, n.readAsDataURL(r)
                            }));
                        case 1:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function l(e, r) {
            var t = /^data:([^;]+);base64,/,
                n = e.match(t);
            if (!n) throw new Error("String base64 inválida. Deve ser uma data URL no formato 'data:mime/type;base64,...'");
            var a = n[1],
                o = e.replace(t, "");
            try {
                for (var s = atob(o), c = new Uint8Array(s.length), u = 0; u < s.length; u++) c[u] = s.charCodeAt(u);
                var i = r;
                if (!i) {
                    var l = function(e) {
                            return {
                                "audio/ogg": "ogg",
                                "audio/mpeg": "mp3",
                                "audio/wav": "wav",
                                "audio/webm": "webm",
                                "image/jpeg": "jpg",
                                "image/png": "png",
                                "image/gif": "gif",
                                "image/webp": "webp",
                                "video/mp4": "mp4",
                                "video/webm": "webm",
                                "application/pdf": "pdf",
                                "text/plain": "txt",
                                "application/json": "json",
                                "application/zip": "zip"
                            } [e] || "bin"
                        }(a),
                        p = Date.now();
                    i = "file_".concat(p, ".").concat(l)
                }
                return new File([c], i, {
                    type: a
                })
            } catch (e) {
                throw new Error("Erro ao converter base64 para arquivo: ".concat(e instanceof Error ? e.message : "Erro desconhecido"))
            }
        }

        function p(e, r) {
            var t = Object.keys(e);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(e);
                r && (n = n.filter(function(r) {
                    return Object.getOwnPropertyDescriptor(e, r).enumerable
                })), t.push.apply(t, n)
            }
            return t
        }

        function f(e) {
            for (var r = 1; r < arguments.length; r++) {
                var t = null != arguments[r] ? arguments[r] : {};
                r % 2 ? p(Object(t), !0).forEach(function(r) {
                    n(e, r, t[r])
                }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : p(Object(t)).forEach(function(r) {
                    Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r))
                })
            }
            return e
        }

        function d(e) {
            if ("string" == typeof e) return e.trim().replace(/^"+|"+$/g, "")
        }

        function h(e) {
            var r;
            try {
                r = "DEV" === e ? "false" : "43d412d0e648a91985b84d107da3ffbaada4f13180c1d45ad068cef46607ee5e"
            } catch (e) {}
            if (void 0 === r) try {
                var t = {
                    NODE_ENV: "production"
                };
                t && (r = "DEV" === e ? t.DEV : t.EMAIL)
            } catch (e) {}
            return d(r)
        }
        var m = "true"; // Força modo desenvolvimento
        var v = "bypass"; // Mock do hash de email
        var x = "undefined" != typeof globalThis ? globalThis.crypto : void 0;
        var b = true; // Ativa o bypass global de licença

        function g(e) {
            return k.apply(this, arguments)
        }

        function k() {
            return (k = o(c().mark(function e(r) {
                var t, n, a, o;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return t = new TextEncoder, n = r.trim().toLowerCase(), e.next = 1, x.subtle.digest("SHA-256", t.encode(n));
                        case 1:
                            return a = e.sent, o = Array.from(new Uint8Array(a)), e.abrupt("return", o.map(function(e) {
                                return e.toString(16).padStart(2, "0")
                            }).join(""));
                        case 2:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function w(e) {
            return new Promise((resolve) => resolve(true));
        }
        function y() {
            return (y = o(c().mark(function e(r) {
                var t;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if (b) {
                                e.next = 1;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 1:
                            if (v) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 2:
                            if (null != x && x.subtle) {
                                e.next = 3;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 3:
                            return e.next = 4, g(r);
                        case 4:
                            return t = e.sent, e.abrupt("return", t === v.toLowerCase());
                        case 5:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function T(e) {
            return {
                ...e,
                EXTENSION: true,
                SAVER: true,
                MATURADOR: true,
                hasPlan: true,
                status: "PAID" // Adicionado para garantir o status visual
            };
        }

        function S() {
            return {
                enabled: b,
                hasEmailHash: Boolean(v)
            }
        }

        function O() {
            return E.apply(this, arguments)
        }

        function E() {
            return (E = o(c().mark(function e() {
                var r, t;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.tabs.query({
                                url: "https://web.whatsapp.com/*"
                            });
                        case 1:
                            return r = e.sent, t = null == r ? void 0 : r[0], e.abrupt("return", "number" == typeof(null == t ? void 0 : t.id) ? t.id : null);
                        case 2:
                            return e.prev = 2, e.catch(0), e.abrupt("return", null);
                        case 3:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 2]
                ])
            }))).apply(this, arguments)
        }

        function A() {
            return j.apply(this, arguments)
        }

        function j() {
            return j = o(c().mark(function r() {
                var t, n, a, s, u, i;
                return c().wrap(function(r) {
                    for (;;) switch (r.prev = r.next) {
                        case 0:
                            return r.next = 1, O();
                        case 1:
                            if (t = r.sent) {
                                r.next = 2;
                                break
                            }
                            return r.abrupt("return", null);
                        case 2:
                            return r.prev = 2, r.next = 3, Promise.race([chrome.tabs.sendMessage(t, {
                                action: "telemetry.getWhatsappEnv"
                            }), new Promise(function(e) {
                                return setTimeout(function() {
                                    return e({
                                        ok: !1,
                                        error: "timeout"
                                    })
                                }, 2500)
                            })]);
                        case 3:
                            if (!(n = r.sent) || !n.ok) {
                                r.next = 4;
                                break
                            }
                            return r.abrupt("return", n.snapshot);
                        case 4:
                            r.next = 6;
                            break;
                        case 5:
                            r.prev = 5, r.catch(2);
                        case 6:
                            if (null != (a = chrome.scripting) && a.executeScript) {
                                r.next = 7;
                                break
                            }
                            return r.abrupt("return", null);
                        case 7:
                            return r.prev = 7, r.next = 8, a.executeScript({
                                target: {
                                    tabId: t
                                },
                                world: "MAIN",
                                func: function() {
                                    var r = o(c().mark(function r() {
                                        var t, n, a, o, s, u, i, l, p, f, d, h, m, v, x;
                                        return c().wrap(function(r) {
                                            for (;;) switch (r.prev = r.next) {
                                                case 0:
                                                    if (n = null === (t = window) || void 0 === t ? void 0 : t.WPP, a = {
                                                            waJsVersion: null,
                                                            waVersion: null,
                                                            windowsBuild: null,
                                                            isBusinessAccount: null
                                                        }, n) {
                                                        r.next = 1;
                                                        break
                                                    }
                                                    return r.abrupt("return", a);
                                                case 1:
                                                    return "string" == typeof n.version && (a.waJsVersion = n.version), r.prev = 2, r.next = 3, null === (o = n.conn) || void 0 === o || null === (s = o.getBuildConstants) || void 0 === s ? void 0 : s.call(o);
                                                case 3:
                                                    (u = r.sent) && "object" === e(u) && (i = u.VERSION_STR, l = u.WINDOWS_BUILD, "string" == typeof i && (a.waVersion = i), "string" == typeof l && (a.windowsBuild = l)), r.next = 5;
                                                    break;
                                                case 4:
                                                    r.prev = 4, r.catch(2);
                                                case 5:
                                                    if (r.prev = 5, !(m = null === (p = n.conn) || void 0 === p || null === (f = p.getMyUserId) || void 0 === f ? void 0 : f.call(p))) {
                                                        r.next = 7;
                                                        break
                                                    }
                                                    return r.next = 6, null === (d = n.contact) || void 0 === d || null === (h = d.get) || void 0 === h ? void 0 : h.call(d, m);
                                                case 6:
                                                    x = r.sent, r.next = 8;
                                                    break;
                                                case 7:
                                                    x = void 0;
                                                case 8:
                                                    v = x, a.isBusinessAccount = !(null == v || !v.isBusiness) || !(null == v || !v.isEnterprise) || !(null == v || !v.isVerifiedBusiness), r.next = 10;
                                                    break;
                                                case 9:
                                                    r.prev = 9, r.catch(5);
                                                case 10:
                                                    return r.abrupt("return", a);
                                                case 11:
                                                case "end":
                                                    return r.stop()
                                            }
                                        }, r, null, [
                                            [2, 4],
                                            [5, 9]
                                        ])
                                    }));
                                    return function() {
                                        return r.apply(this, arguments)
                                    }
                                }()
                            });
                        case 8:
                            return u = r.sent, i = null == u || null === (s = u[0]) || void 0 === s ? void 0 : s.result, r.abrupt("return", null != i ? i : null);
                        case 9:
                            return r.prev = 9, r.catch(7), r.abrupt("return", null);
                        case 10:
                        case "end":
                            return r.stop()
                    }
                }, r, null, [
                    [2, 5],
                    [7, 9]
                ])
            })), j.apply(this, arguments)
        }

        function P(e, r) {
            var t = Object.keys(e);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(e);
                r && (n = n.filter(function(r) {
                    return Object.getOwnPropertyDescriptor(e, r).enumerable
                })), t.push.apply(t, n)
            }
            return t
        }

        function R(e) {
            for (var r = 1; r < arguments.length; r++) {
                var t = null != arguments[r] ? arguments[r] : {};
                r % 2 ? P(Object(t), !0).forEach(function(r) {
                    n(e, r, t[r])
                }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : P(Object(t)).forEach(function(r) {
                    Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r))
                })
            }
            return e
        }
        var _ = "/telemetry/environment",
            M = "https://api.revzap.com.br",
            D = "true" === "MISSING_ENV_VAR".DEBUG_TELEMETRY,
            I = "accessToken",
            N = "telemetry.lastReportedForTokenHash",
            V = null,
            B = !1;

        function C(e) {
            for (var r = arguments.length, t = new Array(r > 1 ? r - 1 : 0), n = 1; n < r; n++) t[n - 1] = arguments[n];
            var a, o;
            b ? (a = console).log.apply(a, [e].concat(t)) : D && (o = console).log.apply(o, [e].concat(t))
        }

        function L(e) {
            return z.apply(this, arguments)
        }

        function z() {
            return (z = o(c().mark(function e(r) {
                var t, n, a;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return t = (new TextEncoder).encode(r), e.next = 1, crypto.subtle.digest("SHA-256", t);
                        case 1:
                            return n = e.sent, a = Array.from(new Uint8Array(n)), e.abrupt("return", a.map(function(e) {
                                return e.toString(16).padStart(2, "0")
                            }).join(""));
                        case 2:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function U(e) {
            switch (e) {
                case "win":
                case "windows":
                    return "Windows";
                case "mac":
                case "macos":
                    return "macOS";
                case "android":
                    return "Android";
                case "cros":
                    return "ChromeOS";
                case "linux":
                    return "Linux";
                case "openbsd":
                    return "OpenBSD";
                default:
                    return "string" == typeof e && e.length ? e : "Unknown"
            }
        }

        function F(e, r, t) {
            var n = r || "",
                a = t || "";
            if (!n || !a) switch (e) {
                case "x86-64":
                    n = n || "x86_64", a = a || "64";
                    break;
                case "x86-32":
                    n = n || "x86", a = a || "32";
                    break;
                case "arm":
                    n = n || "arm", a = a || "unknown";
                    break;
                case "arm64":
                    n = n || "arm64", a = a || "64";
                    break;
                case "mips":
                    n = n || "mips", a = a || "unknown";
                    break;
                case "mips64":
                    n = n || "mips64", a = a || "64"
            }
            return {
                architecture: n || "unknown",
                bitness: a || "unknown"
            }
        }

        function H(e, r) {
            var t = e && e.length ? e : r || [],
                n = t.find(function(e) {
                    return e.brand && "Chromium" !== e.brand && "Not.A/Brand" !== e.brand && "Not;A=Brand" !== e.brand
                }) || t[0];
            if (null != n && n.brand && null != n && n.version) return {
                name: n.brand,
                versionFull: n.version
            };
            var a = navigator.userAgent || "",
                o = a.match(/Edg\/([0-9.]+)/);
            if (o) return {
                name: "Microsoft Edge",
                versionFull: o[1]
            };
            var s = a.match(/OPR\/([0-9.]+)/);
            if (s) return {
                name: "Opera",
                versionFull: s[1]
            };
            var c = a.match(/Chrome\/([0-9.]+)/);
            if (c) return {
                name: "Chrome",
                versionFull: c[1]
            };
            var u = a.match(/Firefox\/([0-9.]+)/);
            if (u) return {
                name: "Firefox",
                versionFull: u[1]
            };
            var i = a.match(/Version\/([0-9.]+).*Safari/);
            return i ? {
                name: "Safari",
                versionFull: i[1]
            } : {
                name: "Unknown",
                versionFull: ""
            }
        }

        function G() {
            return J.apply(this, arguments)
        }

        function J() {
            return (J = o(c().mark(function e() {
                var r, t, n, a, o, s, u, i, l, p, f, d, h, m;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if (null == (n = navigator.userAgentData) || !n.getHighEntropyValues) {
                                e.next = 5;
                                break
                            }
                            return e.prev = 1, e.next = 2, n.getHighEntropyValues(["fullVersionList", "platform", "platformVersion", "architecture", "bitness"]);
                        case 2:
                            l = e.sent, i = l.fullVersionList, a = l.platform, o = l.platformVersion, s = l.architecture, u = l.bitness, e.next = 4;
                            break;
                        case 3:
                            e.prev = 3, e.catch(1);
                        case 4:
                            e.next = 6;
                            break;
                        case 5:
                            a = null == n ? void 0 : n.platform;
                        case 6:
                            return p = null, e.prev = 7, e.next = 8, chrome.runtime.getPlatformInfo();
                        case 8:
                            p = e.sent, e.next = 10;
                            break;
                        case 9:
                            e.prev = 9, e.catch(7), p = null;
                        case 10:
                            return f = H(i, null == n ? void 0 : n.brands), d = U((null === (r = p) || void 0 === r ? void 0 : r.os) || a), h = R({
                                name: d
                            }, o ? {
                                platformVersion: o
                            } : {}), m = F(null === (t = p) || void 0 === t ? void 0 : t.arch, s, u), e.abrupt("return", {
                                browser: f,
                                os: h,
                                arch: m
                            });
                        case 11:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 3],
                    [7, 9]
                ])
            }))).apply(this, arguments)
        }

        function W() {
            return q.apply(this, arguments)
        }

        function q() {
            return (q = o(c().mark(function e() {
                var r, t;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if (!V) {
                                e.next = 1;
                                break
                            }
                            return e.abrupt("return", V);
                        case 1:
                            return e.prev = 1, e.next = 2, chrome.storage.session.get(N);
                        case 2:
                            if (r = e.sent, "string" != typeof(t = null == r ? void 0 : r[N]) || !t.length) {
                                e.next = 3;
                                break
                            }
                            return V = t, e.abrupt("return", t);
                        case 3:
                            e.next = 5;
                            break;
                        case 4:
                            e.prev = 4, e.catch(1);
                        case 5:
                            return e.abrupt("return", null);
                        case 6:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 4]
                ])
            }))).apply(this, arguments)
        }

        function Y(e) {
            return X.apply(this, arguments)
        }

        function X() {
            return (X = o(c().mark(function e(r) {
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return V = r, e.prev = 1, e.next = 2, chrome.storage.session.set(n({}, N, r));
                        case 2:
                            e.next = 4;
                            break;
                        case 3:
                            e.prev = 3, e.catch(1);
                        case 4:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 3]
                ])
            }))).apply(this, arguments)
        }

        function $() { return Promise.resolve(); }
        function K() {
            return (K = o(c().mark(function e(r, t) {
                var n, a;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if (M) {
                                e.next = 1;
                                break
                            }
                            return e.abrupt("return");
                        case 1:
                            return n = new AbortController, a = setTimeout(function() {
                                return n.abort()
                            }, 8e3), e.prev = 2, e.next = 3, fetch("".concat(M).concat(_), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(t)
                                },
                                body: JSON.stringify(r),
                                signal: n.signal
                            });
                        case 3:
                            return e.prev = 3, clearTimeout(a), e.finish(3);
                        case 4:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [2, , 3, 4]
                ])
            }))).apply(this, arguments)
        }

        function Q() { return Promise.resolve(); }

        function Z() {
            return (Z = o(c().mark(function e(r) {
                var t, n, a, o, s, u, i, l, p;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if (t = r.trim()) {
                                e.next = 1;
                                break
                            }
                            return e.abrupt("return");
                        case 1:
                            return e.next = 2, L(t);
                        case 2:
                            return n = e.sent, e.next = 3, W();
                        case 3:
                            if (!(a = e.sent) || a !== n) {
                                e.next = 4;
                                break
                            }
                            return e.abrupt("return");
                        case 4:
                            return b && console.log("[telemetry] reporting for token", {
                                tokenHash: n
                            }), e.next = 5, A();
                        case 5:
                            if (o = e.sent) {
                                e.next = 8;
                                break
                            }
                            return e.next = 6, new Promise(function(e) {
                                return setTimeout(e, 700)
                            });
                        case 6:
                            return e.next = 7, A();
                        case 7:
                            o = e.sent;
                        case 8:
                            if (o) {
                                e.next = 9;
                                break
                            }
                            return b && console.log("[telemetry] WhatsApp env not available; skipping", {
                                tokenHash: n
                            }), C("[telemetry] WhatsApp tab/env not available; skipping report"), e.abrupt("return");
                        case 9:
                            return e.next = 10, G();
                        case 10:
                            return s = e.sent, u = s.browser, i = s.os, l = s.arch, p = {
                                timestamp: (new Date).toISOString(),
                                extensionVersion: chrome.runtime.getManifest().version,
                                sessionToken: t,
                                browser: u,
                                os: i,
                                arch: l,
                                whatsapp: o
                            }, b && console.log("[telemetry] environment snapshot", {
                                timestamp: p.timestamp,
                                extensionVersion: p.extensionVersion,
                                browser: p.browser,
                                os: p.os,
                                arch: p.arch,
                                whatsapp: p.whatsapp,
                                sessionTokenHash: n
                            }), e.prev = 11, e.next = 12, $(p, t);
                        case 12:
                            return e.next = 13, Y(n);
                        case 13:
                            b && console.log("[telemetry] report sent", {
                                tokenHash: n,
                                url: "".concat(M || "").concat(_)
                            }), C("[telemetry] report sent", {
                                tokenHash: n,
                                url: "".concat(M || "").concat(_)
                            }), e.next = 15;
                            break;
                        case 14:
                            e.prev = 14, e.catch(11), b && console.log("[telemetry] report failed (silent)", {
                                tokenHash: n
                            }), C("[telemetry] report failed (silent)", {
                                tokenHash: n
                            });
                        case 15:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [11, 14]
                ])
            }))).apply(this, arguments)
        }

        function ee() {
            return (ee = o(c().mark(function e(r, t) {
                var n, a, o;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if ("local" === t) {
                                e.next = 1;
                                break
                            }
                            return e.abrupt("return");
                        case 1:
                            if (n = r[I]) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return");
                        case 2:
                            if (a = "string" == typeof n.oldValue ? n.oldValue : "", o = "string" == typeof n.newValue ? n.newValue : "", !a.trim()) {
                                e.next = 3;
                                break
                            }
                            return e.abrupt("return");
                        case 3:
                            if (o.trim()) {
                                e.next = 4;
                                break
                            }
                            return e.abrupt("return");
                        case 4:
                            return b && console.log("[telemetry] detected accessToken change empty->filled"), C("[telemetry] detected accessToken change empty->filled"), e.prev = 5, e.next = 6, Q(o);
                        case 6:
                            e.next = 8;
                            break;
                        case 7:
                            e.prev = 7, e.catch(5);
                        case 8:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [5, 7]
                ])
            }))).apply(this, arguments)
        }

        function re() {
            return (re = o(c().mark(function e() {
                var r, t;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get(I);
                        case 1:
                            if (r = e.sent, "string" != typeof(t = null == r ? void 0 : r[I]) || !t.trim()) {
                                e.next = 2;
                                break
                            }
                            return b && console.log("[telemetry] accessToken already present on startup"), C("[telemetry] accessToken already present on startup"), e.next = 2, Q(t);
                        case 2:
                            e.next = 4;
                            break;
                        case 3:
                            e.prev = 3, e.catch(0);
                        case 4:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 3]
                ])
            }))).apply(this, arguments)
        }

        function te(e, r) {
            var t = Object.keys(e);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(e);
                r && (n = n.filter(function(r) {
                    return Object.getOwnPropertyDescriptor(e, r).enumerable
                })), t.push.apply(t, n)
            }
            return t
        }

        function ne(e) {
            for (var r = 1; r < arguments.length; r++) {
                var t = null != arguments[r] ? arguments[r] : {};
                r % 2 ? te(Object(t), !0).forEach(function(r) {
                    n(e, r, t[r])
                }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : te(Object(t)).forEach(function(r) {
                    Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r))
                })
            }
            return e
        }
        var ae = function() {},
            oe = function() {},
            se = "https://api.revzap.com.br",
            ce = function(e) {
                return e.TRIAL_NOT_STARTED = "TRIAL_NOT_STARTED", e.TRIAL_ACTIVE = "TRIAL_ACTIVE", e.TRIAL_EXPIRED = "TRIAL_EXPIRED", e
            }(ce || {}),
            ue = 0,
            ie = {
                logged: true,
                permissions: ["EXTENSION", "SAVER", "MATURADOR"],
                hasPlan: true,
                plan: "PREMIUM"
            },
            le = Promise.resolve();

        function pe(e, r) {
            return fe.apply(this, arguments)
        }

        function fe() {
            return (fe = o(c().mark(function e(r, t) {
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            ie.logged = true;
                            ie.hasPlan = true;
                            ie.permissions = ["EXTENSION", "SAVER", "MATURADOR"];
                            return e.abrupt("return", ie);
                        case 1:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }
        var de = function(e) {
            return e.replace(/@(lid|c\.us|g\.us)$/g, "").trim()
        };

        function he() {
            chrome.alarms.create("session", {
                periodInMinutes: 1
            }), chrome.alarms.create("validate-trial", {
                periodInMinutes: 1
            })
        }

        function me() {
            return ve.apply(this, arguments)
        }

        function ve() {
            return (ve = o(c().mark(function e() {
                var r, t, n, a, o, s, u, i, l;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, ae("[Maturador] Verificando se maturador precisa ser reiniciado..."), e.next = 1, chrome.storage.local.get("maturadorStatus");
                        case 1:
                            if (r = e.sent, null != (t = r.maturadorStatus) && t.ativo) {
                                e.next = 11;
                                break
                            }
                            return ae("[Maturador] Status não encontrado no storage, verificando no DB..."), e.next = 2, ge();
                        case 2:
                            if (null == (n = e.sent) || !n.id) {
                                e.next = 10;
                                break
                            }
                            return e.prev = 3, e.next = 4, chrome.tabs.sendMessage(n.id, {
                                action: "maturador.getConfig"
                            });
                        case 4:
                            if (null == (o = e.sent) || !o.ok || null === (a = o.config) || void 0 === a || !a.ativo) {
                                e.next = 6;
                                break
                            }
                            return ae("[Maturador] Maturador ativo encontrado no DB, atualizando storage..."), e.next = 5, chrome.storage.local.set({
                                maturadorStatus: {
                                    ativo: !0,
                                    whatsapp: o.config.whatsapp || "",
                                    delayMin: o.config.intervaloMin || 1,
                                    delayMax: o.config.intervaloMax || 2,
                                    updatedAt: Date.now()
                                }
                            });
                        case 5:
                            e.next = 7;
                            break;
                        case 6:
                            return ae("[Maturador] Maturador não está ativo no DB"), e.abrupt("return");
                        case 7:
                            e.next = 9;
                            break;
                        case 8:
                            return e.prev = 8, i = e.catch(3), ae("[Maturador] Erro ao verificar DB:", i), e.abrupt("return");
                        case 9:
                            e.next = 11;
                            break;
                        case 10:
                            return ae("[Maturador] Nenhuma aba ativa para verificar"), e.abrupt("return");
                        case 11:
                            return e.next = 12, chrome.storage.local.get("maturadorStatus");
                        case 12:
                            s = e.sent, null != (u = s.maturadorStatus) && u.ativo ? (ae("[Maturador] Maturador estava ativo, reiniciando..."), setTimeout(function() {
                                Fe(function() {})
                            }, 5e3)) : ae("[Maturador] Maturador não está ativo, não reinicia"), e.next = 14;
                            break;
                        case 13:
                            e.prev = 13, l = e.catch(0), ae("[Maturador] Erro ao verificar maturador:", l);
                        case 14:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 13],
                    [3, 8]
                ])
            }))).apply(this, arguments)
        }

        function xe() {
            return be.apply(this, arguments)
        }

        function be() {
            return (be = o(c().mark(function e() {
                var r, t, n;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (r = e.sent, r.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 2:
                            if (ie.logged) {
                                e.next = 3;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 3:
                            if (!ie.hasPlan) {
                                e.next = 4;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 4:
                            if (ie.trialEndsAt) {
                                e.next = 5;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 5:
                            if (ie.trialStatus === ce.TRIAL_ACTIVE) {
                                e.next = 6;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 6:
                            if (t = new Date(ie.trialEndsAt || ""), n = new Date, !(t && t < n)) {
                                e.next = 8;
                                break
                            }
                            return e.next = 7, Se();
                        case 7:
                            return e.next = 8, pe({
                                trialStatus: ce.TRIAL_EXPIRED
                            }, "validateTrial:expired");
                        case 8:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function ge(e) {
            return ke.apply(this, arguments)
        }

        function ke() {
            return (ke = o(c().mark(function e(r) {
                var t, n;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, chrome.tabs.query({
                                url: "https://web.whatsapp.com/*"
                            });
                        case 1:
                            return t = e.sent, n = t[0], r && r(n), e.abrupt("return", n);
                        case 2:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function we() {
            return ye.apply(this, arguments)
        }

        function ye() {
            return ye = o(c().mark(function e() {
                var r, t = arguments;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return r = t.length > 0 && void 0 !== t[0] ? t[0] : "resetSession", ie = {
                                logged: !1
                            }, e.next = 1, chrome.storage.local.remove(["accessToken", "refreshToken"]);
                        case 1:
                            return e.next = 2, pe({
                                logged: !1,
                                email: void 0,
                                permissions: [],
                                role: void 0,
                                hasPlan: void 0,
                                trialStatus: void 0,
                                trialEndsAt: void 0
                            }, r);
                        case 2:
                        case "end":
                            return e.stop()
                    }
                }, e)
            })), ye.apply(this, arguments)
        }

        function Te() {
            return (Te = o(c().mark(function e(r, t, n) {
                var a, o, s, i, p, f, d, h, m;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (a = e.sent, o = a.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", n({
                                ok: !1,
                                error: "Você precisa estar logado para converter áudios.",
                                message: "Você precisa estar logado para converter áudios."
                            }));
                        case 2:
                            if (e.prev = 2, s = l(r, t), (i = new FormData).append("audio", s), s) {
                                e.next = 3;
                                break
                            }
                            return e.abrupt("return", n({
                                ok: !1,
                                message: "Erro ao converter áudio"
                            }));
                        case 3:
                            return e.next = 4, fetch("".concat(se, "/extension/convert-audio"), {
                                method: "POST",
                                body: i,
                                headers: {
                                    Authorization: "Bearer ".concat(o)
                                }
                            });
                        case 4:
                            if ((p = e.sent).ok) {
                                e.next = 6;
                                break
                            }
                            return e.next = 5, p.json();
                        case 5:
                            return f = e.sent, e.abrupt("return", n({
                                ok: !1,
                                message: f.message || "Erro ao converter"
                            }));
                        case 6:
                            return e.next = 7, p.blob();
                        case 7:
                            return d = e.sent, e.next = 8, u(d);
                        case 8:
                            h = e.sent, n({
                                ok: !0,
                                base64: h
                            }), e.next = 10;
                            break;
                        case 9:
                            e.prev = 9, m = e.catch(2), console.error("Erro ao converter áudio:", m), n({
                                ok: !1,
                                message: "Ocorreu um erro ao tentar converter o áudio!"
                            });
                        case 10:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [2, 9]
                ])
            }))).apply(this, arguments)
        }

        function Se() {
            return Oe.apply(this, arguments)
        }

        function Oe() {
            return (Oe = o(c().mark(function e() {
                var r, t, n;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (r = e.sent, t = r.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/free-tier/finish"), {
                                method: "POST",
                                headers: {
                                    Authorization: "Bearer ".concat(t)
                                }
                            });
                        case 3:
                            return n = e.sent, e.next = 4, n.json();
                        case 4:
                            if (e.sent.ok) {
                                e.next = 6;
                                break
                            }
                            if (!(++ue > 3)) {
                                e.next = 5;
                                break
                            }
                            if (!(n.status >= 400 && n.status < 500)) {
                                e.next = 5;
                                break
                            }
                            return ue = 0, e.next = 5, we();
                        case 5:
                            return e.abrupt("return", !1);
                        case 6:
                            return ue = 0, e.abrupt("return", !0);
                        case 7:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function Ee() {
            return Ae.apply(this, arguments)
        }

        function Ae() {
            return (Ae = o(c().mark(function e() {
                var r, t, n, a, o, s, u, i, l, p, f, d, h, m, v, x;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (t = e.sent, n = t.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/user"), {
                                headers: {
                                    Authorization: "Bearer ".concat(n)
                                }
                            });
                        case 3:
                            return a = e.sent, e.next = 4, a.json();
                        case 4:
                            if ((o = e.sent).ok) {
                                e.next = 6;
                                break
                            }
                            if (!(++ue > 3)) {
                                e.next = 5;
                                break
                            }
                            if (!(a.status >= 400 && a.status < 500)) {
                                e.next = 5;
                                break
                            }
                            return ue = 0, e.next = 5, we();
                        case 5:
                            return e.abrupt("return", !1);
                        case 6:
                            return ue = 0, s = o.user.email, u = o.permissions || [], i = o.user.role || "USER", l = o.user.trialStatus, p = o.user.trialEndsAt, f = o.user.statusReview, d = o.user.scoreReview, h = o.user.msgReview, m = Array.isArray(null === (r = o.user) || void 0 === r ? void 0 : r.subscriptions) ? o.user.subscriptions : [], ae("[getUser] Calculando hasPlan:", "\n  subscriptions:", m, "\n  trialStatus:", l, "\n  permissions:", u), v = m.some(function(e) {
                                var r = null == e ? void 0 : e.expiresAt;
                                if (!r || (new Date(r).getTime(), Date.now()), !r) return !0;
                                var t = new Date(r);
                                return !Number.isNaN(t.getTime()) && t.getTime() > Date.now()
                            }), x = v || Array.isArray(u) && u.length > 0 && l !== ce.TRIAL_ACTIVE, ae("[getUser] Resultado:", "\n  hasNonExpiredSubscription:", v, "\n  hasPlan:", x, "\n  trialStatus:", l), e.next = 7, pe({
                                logged: !0,
                                email: s,
                                permissions: u,
                                role: i,
                                hasPlan: x,
                                trialStatus: null != l ? l : void 0,
                                trialEndsAt: null != p ? p : void 0,
                                statusReview: null != f ? f : void 0,
                                scoreReview: null != d ? d : void 0,
                                msgReview: null != h ? h : void 0
                            }, "getUser:/user");
                        case 7:
                            return e.abrupt("return", !0);
                        case 8:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function je() {
            return Pe.apply(this, arguments)
        }

        function Pe() {
            return (Pe = o(c().mark(function e() {
                var r, t, n, a, o, s;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, chrome.storage.local.get("refreshToken");
                        case 1:
                            if (r = e.sent, t = r.refreshToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/session/refresh"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    refreshToken: t
                                })
                            });
                        case 3:
                            return n = e.sent, e.next = 4, n.json();
                        case 4:
                            if ((a = e.sent).ok) {
                                e.next = 6;
                                break
                            }
                            if (!(++ue > 3)) {
                                e.next = 5;
                                break
                            }
                            if (!(n.status >= 400 && n.status < 500)) {
                                e.next = 5;
                                break
                            }
                            return ue = 0, e.next = 5, we();
                        case 5:
                            return e.abrupt("return", !1);
                        case 6:
                            if (ue = 0, o = a.accessToken, s = a.refreshToken) {
                                e.next = 7;
                                break
                            }
                            return e.abrupt("return", !1);
                        case 7:
                            return e.next = 8, chrome.storage.local.set({
                                refreshToken: s
                            });
                        case 8:
                            if (ie.lastRefresh = new Date, !o) {
                                e.next = 9;
                                break
                            }
                            return e.next = 9, chrome.storage.local.set({
                                accessToken: o
                            });
                        case 9:
                            return e.abrupt("return", !0);
                        case 10:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function Re() {
            return (Re = o(c().mark(function e(r, t, n) {
                var a, o;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, fetch("".concat(se, "/session/confirm-code"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    code: r,
                                    email: t
                                })
                            });
                        case 1:
                            return a = e.sent, e.next = 2, a.json();
                        case 2:
                            o = e.sent, a.ok || n({
                                ok: !1,
                                message: o.message || "Ocorreu um erro ao tentar validar o código!"
                            }), n({
                                ok: !0,
                                message: "Código validado com sucesso!",
                                token: o.token
                            });
                        case 3:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function _e() {
            return (_e = o(c().mark(function e(r, t, n) {
                var a, o;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, fetch("".concat(se, "/session/change-password"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    newPassword: r,
                                    token: t
                                })
                            });
                        case 1:
                            return a = e.sent, e.next = 2, a.json();
                        case 2:
                            o = e.sent, a.ok || n({
                                ok: !1,
                                message: o.message || "Ocorreu um erro ao tentar alterar a senha!"
                            }), n({
                                ok: !0,
                                message: "Senha alterada com sucesso!"
                            });
                        case 3:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function Me() {
            return (Me = o(c().mark(function e(r, t) {
                var n, a;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.next = 1, fetch("".concat(se, "/session/forget-password"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    email: r
                                })
                            });
                        case 1:
                            return n = e.sent, e.next = 2, n.json();
                        case 2:
                            a = e.sent, n.ok || t({
                                ok: !1,
                                message: a.message || "Ocorreu um erro ao tentar resetar a senha!"
                            }), t({
                                ok: !0,
                                message: "Email de recuperação enviado com sucesso!"
                            });
                        case 3:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))).apply(this, arguments)
        }

        function De() {
            return (De = o(c().mark(function e(r) {
                var t, n, a;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("cachedSession");
                        case 1:
                            if (!(t = e.sent).cachedSession) {
                                e.next = 2;
                                break
                            }
                            return r(t.cachedSession), o(c().mark(function e() {
                                return c().wrap(function(e) {
                                    for (;;) switch (e.prev = e.next) {
                                        case 0:
                                            if (ie.logged) {
                                                e.next = 3;
                                                break
                                            }
                                            if (ie.lastRefresh && !((new Date).getTime() - ie.lastRefresh.getTime() > 3e5)) {
                                                e.next = 1;
                                                break
                                            }
                                            return e.next = 1, je();
                                        case 1:
                                            return e.next = 2, Ee();
                                        case 2:
                                            return e.next = 3, xe();
                                        case 3:
                                        case "end":
                                            return e.stop()
                                    }
                                }, e)
                            }))().catch(function(e) {
                                console.error("[Session] Erro ao sincronizar sessão:", e)
                            }), e.abrupt("return");
                        case 2:
                            e.next = 4;
                            break;
                        case 3:
                            e.prev = 3, a = e.catch(0), console.error("[Session] Erro ao carregar cache:", a);
                        case 4:
                            if (ie.logged) {
                                e.next = 7;
                                break
                            }
                            if (ie.lastRefresh && !((new Date).getTime() - ie.lastRefresh.getTime() > 3e5)) {
                                e.next = 5;
                                break
                            }
                            return e.next = 5, je();
                        case 5:
                            return e.next = 6, Ee();
                        case 6:
                            return e.next = 7, xe();
                        case 7:
                            n = {
                                logged: ie.logged,
                                email: ie.email,
                                permissions: ie.permissions,
                                hasPlan: ie.hasPlan,
                                trialStatus: ie.trialStatus,
                                trialEndsAt: ie.trialEndsAt
                            }, r(n);
                        case 8:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 3]
                ])
            }))).apply(this, arguments)
        }

        function Ie() {
            return (Ie = o(c().mark(function e(r, t) {
                var n, a, o, s, u, i, l, p, f, d, h, m, v, x, g, k, w, y, T, S, O, E, A, j, P;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return n = r.email, a = r.password, o = r.passwordConfirm, e.prev = 1, m = btoa("".concat(n || "", ":").concat(o ? "" : a || "")), v = {}, o && (v.password = o), e.next = 2, fetch("".concat(se, "/session/sign-in"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Basic ".concat(m)
                                },
                                body: JSON.stringify(v)
                            });
                        case 2:
                            return x = e.sent, e.next = 3, x.json();
                        case 3:
                            if (g = e.sent, x.ok) {
                                e.next = 5;
                                break
                            }
                            if (!g.sessionLimitReached) {
                                e.next = 4;
                                break
                            }
                            return t({
                                sessionLimitReached: !0,
                                sessions: g.sessions || [],
                                maxSessions: null !== (k = g.maxSessions) && void 0 !== k ? k : 1,
                                activeSessions: null !== (w = g.activeSessions) && void 0 !== w ? w : 0,
                                upgradeRequired: null !== (y = g.upgradeRequired) && void 0 !== y && y,
                                message: g.message || "Limite de sessões atingido!"
                            }), e.abrupt("return");
                        case 4:
                            throw new Error(g.message || "Ocorreu um erro ao fazer login. Tente novamente!");
                        case 5:
                            return b && console.log(g), T = g.accessToken, S = g.refreshToken, e.next = 6, chrome.storage.local.set({
                                accessToken: T,
                                refreshToken: S
                            });
                        case 6:
                            return O = [], E = Array.isArray(null === (s = g.user) || void 0 === s ? void 0 : s.subscriptions) ? g.user.subscriptions : [], ae("[handleSessionSignIn] Calculando hasPlan:", "\n  subscriptions:", E, "\n  trialStatus:", null === (u = g.user) || void 0 === u ? void 0 : u.trialStatus, "\n  signInPermissions:", O), A = E.some(function(e) {
                                var r = null == e ? void 0 : e.expiresAt;
                                if (!r || (new Date(r).getTime(), Date.now()), !r) return !0;
                                var t = new Date(r);
                                return !Number.isNaN(t.getTime()) && t.getTime() > Date.now()
                            }), j = A || O.length > 0 && (null === (i = g.user) || void 0 === i ? void 0 : i.trialStatus) !== ce.TRIAL_ACTIVE, ae("[handleSessionSignIn] Resultado:", "\n  hasNonExpiredSubscription:", A, "\n  hasPlan:", j, "\n  trialStatus:", null === (l = g.user) || void 0 === l ? void 0 : l.trialStatus), e.next = 7, pe({
                                logged: !0,
                                email: n,
                                permissions: O,
                                hasPlan: j,
                                trialEndsAt: null !== (p = null === (f = g.user) || void 0 === f ? void 0 : f.trialEndsAt) && void 0 !== p ? p : void 0,
                                trialStatus: null !== (d = null === (h = g.user) || void 0 === h ? void 0 : h.trialStatus) && void 0 !== d ? d : void 0,
                                lastRefresh: new Date
                            }, "session.sign-in:tokens");
                        case 7:
                            return e.next = 8, Ee();
                        case 8:
                            return e.next = 9, xe();
                        case 9:
                            t(!0), e.next = 11;
                            break;
                        case 10:
                            e.prev = 10, P = e.catch(1), t({
                                error: P.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 11:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 10]
                ])
            }))).apply(this, arguments)
        }

        function Ne() {
            return (Ne = o(c().mark(function e(r, t) {
                var n, a, o, s, u, i, l;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return n = r.sessionId, a = r.email, o = r.password, e.prev = 1, s = btoa("".concat(a || "", ":").concat(o || "")), e.next = 2, fetch("".concat(se, "/session/revoke/").concat(n), {
                                method: "DELETE",
                                headers: {
                                    Authorization: "Basic ".concat(s)
                                }
                            });
                        case 2:
                            return u = e.sent, e.next = 3, u.json();
                        case 3:
                            if (i = e.sent, u.ok) {
                                e.next = 4;
                                break
                            }
                            throw new Error(i.message || "Erro ao revogar sessão.");
                        case 4:
                            t({
                                ok: !0
                            }), e.next = 6;
                            break;
                        case 5:
                            e.prev = 5, l = e.catch(1), t({
                                error: l.message || "Erro ao revogar sessão. Tente novamente!"
                            });
                        case 6:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 5]
                ])
            }))).apply(this, arguments)
        }

        function Ve() {
            return (Ve = o(c().mark(function e(r, t) {
                var n, a, o;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return n = r.email, e.prev = 1, e.next = 2, fetch("".concat(se, "/session/email"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                body: JSON.stringify({
                                    email: n
                                })
                            });
                        case 2:
                            return a = e.sent, e.next = 3, a.json();
                        case 3:
                            o = e.sent, t(o), e.next = 5;
                            break;
                        case 4:
                            e.prev = 4, e.catch(1), t({
                                error: "Ocorreu um erro ao tentar buscar pelo email! " + se
                            });
                        case 5:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 4]
                ])
            }))).apply(this, arguments)
        }

        function Be() {
            return (Be = o(c().mark(function e(r) {
                var t, n;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.prev = 1, e.next = 2, chrome.storage.local.get("accessToken");
                        case 2:
                            if (!(t = e.sent).accessToken) {
                                e.next = 3;
                                break
                            }
                            return e.next = 3, fetch("".concat(se, "/session/sign-out"), {
                                method: "POST",
                                headers: {
                                    Authorization: "Bearer ".concat(t.accessToken)
                                }
                            }).catch(function(e) {});
                        case 3:
                            e.next = 5;
                            break;
                        case 4:
                            e.prev = 4, n = e.catch(1), oe("[handleSessionLogout] Erro ao chamar sign-out na API:", n);
                        case 5:
                            return e.next = 6, we("logout");
                        case 6:
                            return r(!0), e.abrupt("return");
                        case 7:
                            e.prev = 7, e.catch(0), r(!1);
                        case 8:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 7],
                    [1, 4]
                ])
            }))).apply(this, arguments)
        }

        function Ce() {
            return (Ce = o(c().mark(function e(r, t) {
                var n, a, o, s;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            return n = e.sent, e.next = 2, fetch("".concat(se, "/user/edit"), {
                                method: "PUT",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(n.accessToken)
                                },
                                body: JSON.stringify(r)
                            });
                        case 2:
                            return a = e.sent, e.next = 3, a.json();
                        case 3:
                            if (o = e.sent, a.ok) {
                                e.next = 4;
                                break
                            }
                            throw new Error(o.message || "Ocorreu um erro. Tente novamente!");
                        case 4:
                            t(o), e.next = 6;
                            break;
                        case 5:
                            e.prev = 5, s = e.catch(0), t({
                                error: s.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 6:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 5]
                ])
            }))).apply(this, arguments)
        }

        function Le() {
            return (Le = o(c().mark(function e(r) {
                var t, n, a, o, s;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            if (e.prev = 0, !b || !ie.email) {
                                e.next = 2;
                                break
                            }
                            return e.next = 1, w(ie.email);
                        case 1:
                            if (!e.sent) {
                                e.next = 2;
                                break
                            }
                            return r({
                                ok: !0,
                                temPermissao: !0,
                                maturador: null
                            }), e.abrupt("return");
                        case 2:
                            return e.next = 3, chrome.storage.local.get("accessToken");
                        case 3:
                            if (t = e.sent, n = t.accessToken) {
                                e.next = 4;
                                break
                            }
                            return e.abrupt("return", r({
                                ok: !1,
                                error: "Não autenticado"
                            }));
                        case 4:
                            return e.next = 5, fetch("".concat(se, "/maturador"), {
                                method: "GET",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(n)
                                }
                            });
                        case 5:
                            return a = e.sent, e.next = 6, a.json();
                        case 6:
                            if (o = e.sent, a.ok) {
                                e.next = 7;
                                break
                            }
                            throw new Error(o.message || "Erro ao buscar maturador");
                        case 7:
                            r(o), e.next = 9;
                            break;
                        case 8:
                            e.prev = 8, s = e.catch(0), r({
                                ok: !1,
                                error: s.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 9:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 8]
                ])
            }))).apply(this, arguments)
        }

        function ze() {
            return (ze = o(c().mark(function e(r, t) {
                var n, a, o, s, u;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (n = e.sent, a = n.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", t({
                                ok: !1,
                                error: "Não autenticado"
                            }));
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/maturador"), {
                                method: "PUT",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(a)
                                },
                                body: JSON.stringify(r)
                            });
                        case 3:
                            return o = e.sent, e.next = 4, o.json();
                        case 4:
                            if (s = e.sent, o.ok) {
                                e.next = 5;
                                break
                            }
                            return e.abrupt("return", t({
                                ok: !1,
                                error: s.message || "Erro ao atualizar maturador",
                                status: o.status
                            }));
                        case 5:
                            ae("[Maturador] Estado atualizado no backend:", {
                                whatsapp: r.whatsapp,
                                ligado: r.ligado,
                                delayMin: r.delayMin,
                                delayMax: r.delayMax
                            }), t(s), e.next = 7;
                            break;
                        case 6:
                            e.prev = 6, u = e.catch(0), t({
                                ok: !1,
                                error: u.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 7:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 6]
                ])
            }))).apply(this, arguments)
        }

        function Ue() {
            return (Ue = o(c().mark(function e(r, t) {
                var n, a, o, s, u;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (n = e.sent, a = n.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", t({
                                ok: !1,
                                error: "Não autenticado"
                            }));
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/maturador/update-receptor"), {
                                method: "PUT",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(a)
                                },
                                body: JSON.stringify(r)
                            });
                        case 3:
                            return o = e.sent, e.next = 4, o.json();
                        case 4:
                            if (s = e.sent, o.ok) {
                                e.next = 5;
                                break
                            }
                            throw new Error(s.message || "Erro ao atualizar receptor");
                        case 5:
                            t(s), e.next = 7;
                            break;
                        case 6:
                            e.prev = 6, u = e.catch(0), t({
                                ok: !1,
                                error: u.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 7:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 6]
                ])
            }))).apply(this, arguments)
        }

        function Fe(e) {
            return He.apply(this, arguments)
        }

        function He() {
            return (He = o(c().mark(function e(r) {
                var t, n;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, Ge();
                        case 1:
                            if (t = e.sent) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", r({
                                ok: !1,
                                error: "Erro ao criar shoot do maturador"
                            }));
                        case 2:
                            r({
                                ok: !0,
                                shootId: t.id
                            }), setTimeout(function() {
                                We(t.id)
                            }, 1e3), e.next = 4;
                            break;
                        case 3:
                            e.prev = 3, n = e.catch(0), r({
                                ok: !1,
                                error: n.message || "Erro ao criar shoot"
                            });
                        case 4:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 3]
                ])
            }))).apply(this, arguments)
        }

        function Ge() {
            return Je.apply(this, arguments)
        }

        function Je() {
            return (Je = o(c().mark(function e() {
                var r, t, n, a, o, s, u, i, l, p, f, d, h, m, v, x, b, g;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (t = e.sent, n = t.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", null);
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/maturador"), {
                                method: "GET",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(n)
                                }
                            });
                        case 3:
                            return a = e.sent, e.next = 4, a.json();
                        case 4:
                            if (o = e.sent, a.ok && o.ok && o.temPermissao) {
                                e.next = 5;
                                break
                            }
                            return e.abrupt("return", null);
                        case 5:
                            if (null != (s = null === (r = o.maturador) || void 0 === r ? void 0 : r.find(function(e) {
                                    return !0 === e.ligado
                                })) && s.whatsapp) {
                                e.next = 6;
                                break
                            }
                            return e.abrupt("return", null);
                        case 6:
                            return e.next = 7, fetch("".concat(se, "/maturador/global"), {
                                method: "GET",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(n)
                                }
                            });
                        case 7:
                            return u = e.sent, e.next = 8, u.json();
                        case 8:
                            if (i = e.sent, u.ok && i.numeros && Array.isArray(i.numeros)) {
                                e.next = 9;
                                break
                            }
                            return e.abrupt("return", null);
                        case 9:
                            if (l = de(s.whatsapp), 0 !== (p = i.numeros.filter(function(e) {
                                    return de(e.whatsapp) !== l && !0 === e.ligado
                                }).map(function(e) {
                                    var r = e.whatsapp.replace(/@(lid|c\.us|g\.us)$/g, ""),
                                        t = "@c.us";
                                    return e.whatsapp.includes("@g.us") ? t = "@g.us" : e.whatsapp.includes("@lid") && (t = "@lid"), {
                                        chatId: r,
                                        userId: r,
                                        server: t,
                                        sent: !1,
                                        error: !1,
                                        source: {
                                            type: "spreadsheet",
                                            ids: []
                                        }
                                    }
                                })).length) {
                                e.next = 10;
                                break
                            }
                            return e.abrupt("return", null);
                        case 10:
                            for (f = p.length - 1; f > 0; f--) d = Math.floor(Math.random() * (f + 1)), h = [p[d], p[f]], p[f] = h[0], p[d] = h[1];
                            return e.next = 11, ge();
                        case 11:
                            if (null != (m = e.sent) && m.id) {
                                e.next = 12;
                                break
                            }
                            return e.abrupt("return", null);
                        case 12:
                            return e.prev = 12, e.next = 13, chrome.tabs.sendMessage(m.id, {
                                action: "maturador.getShoots"
                            });
                        case 13:
                            if (null == (v = e.sent) || !v.ok || !v.shoots) {
                                e.next = 14;
                                break
                            }
                            if (null == (x = v.shoots.find(function(e) {
                                    return !0 === e.hidden
                                })) || !x.id) {
                                e.next = 14;
                                break
                            }
                            return e.next = 14, chrome.tabs.sendMessage(m.id, {
                                action: "maturador.deleteShoot",
                                data: {
                                    id: x.id
                                }
                            });
                        case 14:
                            e.next = 16;
                            break;
                        case 15:
                            e.prev = 15, e.catch(12);
                        case 16:
                            return b = {
                                title: "🤖 Maturador Automático",
                                contacts: p,
                                interval: [60 * (s.delayMin || 1), 60 * (s.delayMax || 2)],
                                items: [],
                                status: void 0,
                                hidden: !0,
                                randomizeActions: !1
                            }, e.next = 17, chrome.tabs.sendMessage(m.id, {
                                action: "maturador.createShoot",
                                data: b
                            });
                        case 17:
                            if (null != (g = e.sent) && g.ok && g.shoot) {
                                e.next = 18;
                                break
                            }
                            return e.abrupt("return", null);
                        case 18:
                            return e.abrupt("return", g.shoot);
                        case 19:
                            return e.prev = 19, e.catch(0), e.abrupt("return", null);
                        case 20:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 19],
                    [12, 15]
                ])
            }))).apply(this, arguments)
        }

        function We(e) {
            return qe.apply(this, arguments)
        }

        function qe() {
            return (qe = o(c().mark(function e(r) {
                var t;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, ge();
                        case 1:
                            if (null != (t = e.sent) && t.id) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return");
                        case 2:
                            return e.next = 3, chrome.tabs.sendMessage(t.id, {
                                action: "maturador.startShooting",
                                data: {
                                    shootId: r
                                }
                            });
                        case 3:
                            e.next = 5;
                            break;
                        case 4:
                            e.prev = 4, e.catch(0);
                        case 5:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 4]
                ])
            }))).apply(this, arguments)
        }

        function Ye() {
            return (Ye = o(c().mark(function e(r, t) {
                var n, a, o, s, u;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return t({
                                ok: !0
                            }), e.prev = 1, e.next = 2, chrome.storage.local.get("accessToken");
                        case 2:
                            if (a = e.sent, (o = a.accessToken) && null != r && null !== (n = r.contacts) && void 0 !== n && n.length) {
                                e.next = 3;
                                break
                            }
                            return e.abrupt("return");
                        case 3:
                            return s = new AbortController, u = setTimeout(function() {
                                return s.abort()
                            }, 15e3), e.next = 4, fetch("".concat(se, "/shooting/contacts"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(o)
                                },
                                body: JSON.stringify({
                                    contacts: r.contacts
                                }),
                                signal: s.signal
                            });
                        case 4:
                            clearTimeout(u), e.next = 6;
                            break;
                        case 5:
                            e.prev = 5, e.catch(1);
                        case 6:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [1, 5]
                ])
            }))).apply(this, arguments)
        }

        function Xe() {
            return (Xe = o(c().mark(function e(r, t) {
                var n, a, o, s, u;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (n = e.sent, a = n.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", t({
                                ok: !1,
                                error: "Você precisa estar logado para enviar uma avaliação."
                            }));
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/user/review"), {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json",
                                    Authorization: "Bearer ".concat(a)
                                },
                                body: JSON.stringify({
                                    statusReview: "SUBMITTED",
                                    scoreReview: r.score,
                                    msgReview: r.message || null
                                })
                            });
                        case 3:
                            return o = e.sent, e.next = 4, o.json();
                        case 4:
                            if (s = e.sent, o.ok) {
                                e.next = 5;
                                break
                            }
                            throw new Error(s.message || "Erro ao enviar avaliação");
                        case 5:
                            return e.next = 6, pe({
                                statusReview: "SUBMITTED",
                                scoreReview: r.score,
                                msgReview: r.message || void 0
                            }, "handleReviewSubmit");
                        case 6:
                            t(ne({
                                ok: !0
                            }, s)), e.next = 8;
                            break;
                        case 7:
                            e.prev = 7, u = e.catch(0), t({
                                ok: !1,
                                error: u.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 8:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 7]
                ])
            }))).apply(this, arguments)
        }

        function $e() {
            return ($e = o(c().mark(function e(r) {
                var t, n, a, o, s;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return e.prev = 0, e.next = 1, chrome.storage.local.get("accessToken");
                        case 1:
                            if (t = e.sent, n = t.accessToken) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return", r({
                                ok: !1,
                                error: "Você precisa estar logado."
                            }));
                        case 2:
                            return e.next = 3, fetch("".concat(se, "/reviews"), {
                                method: "GET",
                                headers: {
                                    Authorization: "Bearer ".concat(n)
                                }
                            });
                        case 3:
                            return a = e.sent, e.next = 4, a.json();
                        case 4:
                            if (o = e.sent, a.ok) {
                                e.next = 5;
                                break
                            }
                            throw new Error(o.message || "Erro ao buscar estatísticas");
                        case 5:
                            r(ne({
                                ok: !0
                            }, o)), e.next = 7;
                            break;
                        case 6:
                            e.prev = 6, s = e.catch(0), r({
                                ok: !1,
                                error: s.message || "Ocorreu um erro. Tente novamente!"
                            });
                        case 7:
                        case "end":
                            return e.stop()
                    }
                }, e, null, [
                    [0, 6]
                ])
            }))).apply(this, arguments)
        }
        he(),
            function() {
                if (!B) {
                    B = !0, b && console.log("[telemetry] initEnvironmentReporter", {
                        hasApiBaseUrl: Boolean(M),
                        endpoint: _
                    }), C("[telemetry] initEnvironmentReporter", {
                        hasApiBaseUrl: Boolean(M),
                        endpoint: _
                    });
                    try {
                        chrome.storage.onChanged.addListener(function(e, r) {
                            ! function(e, r) {
                                ee.apply(this, arguments)
                            }(e, r)
                        })
                    } catch (e) {}! function() {
                        re.apply(this, arguments)
                    }()
                }
            }(), chrome.runtime.onStartup.addListener(function() {
                he(), me()
            }), chrome.runtime.onInstalled.addListener(o(c().mark(function e() {
                var r;
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            return he(), e.next = 1, ge();
                        case 1:
                            null != (r = e.sent) && r.id ? (chrome.tabs.reload(r.id), setTimeout(function() {
                                me()
                            }, 8e3)) : setTimeout(function() {
                                me()
                            }, 5e3);
                        case 2:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))), chrome.action.onClicked.addListener(o(c().mark(function e() {
                return c().wrap(function(e) {
                    for (;;) switch (e.prev = e.next) {
                        case 0:
                            ge(function(e) {
                                if (null != e && e.id) e.active || chrome.tabs.update(e.id, {
                                    active: !0
                                });
                                else {
                                    var r = '"2.3000.1029560485" ### npm run launch:local',
                                        t = r ? "https://web.whatsapp.com/?wa_version=".concat(r) : "https://web.whatsapp.com/";
                                    chrome.tabs.create({
                                        url: t
                                    })
                                }
                            });
                        case 1:
                        case "end":
                            return e.stop()
                    }
                }, e)
            }))), chrome.alarms.onAlarm.addListener(function() {
                var e = o(c().mark(function e(r) {
                    return c().wrap(function(e) {
                        for (;;) switch (e.prev = e.next) {
                            case 0:
                                if ("session" !== r.name) {
                                    e.next = 4;
                                    break
                                }
                                return e.next = 1, je();
                            case 1:
                                return e.next = 2, Ee();
                            case 2:
                                return e.next = 3, xe();
                            case 3:
                                ge(function(e) {
                                    null != e && e.id && chrome.tabs.sendMessage(e.id, {
                                        action: "session.updated",
                                        data: {
                                            logged: ie.logged,
                                            email: ie.email,
                                            role: ie.role,
                                            permissions: ie.permissions,
                                            hasPlan: ie.hasPlan,
                                            trialStatus: ie.trialStatus,
                                            trialEndsAt: ie.trialEndsAt,
                                            statusReview: ie.statusReview,
                                            scoreReview: ie.scoreReview,
                                            msgReview: ie.msgReview
                                        }
                                    })
                                }), e.next = 6;
                                break;
                            case 4:
                                if ("validate-trial" !== r.name) {
                                    e.next = 6;
                                    break
                                }
                                return e.next = 5, Ee();
                            case 5:
                                return e.next = 6, xe();
                            case 6:
                            case "end":
                                return e.stop()
                        }
                    }, e)
                }));
                return function(r) {
                    return e.apply(this, arguments)
                }
            }()), chrome.runtime.onMessage.addListener(function(e, r, t) {
                switch (e.action) {
                    case "extension.convert-audio":
                        return function(e, r, t) {
                            Te.apply(this, arguments)
                        }(e.data.file, e.data.fileName, t), !0;
                    case "session":
                        return function(e) {
                            De.apply(this, arguments)
                        }(t), !0;
                    case "session.sign-in":
                        return function(e, r) {
                            Ie.apply(this, arguments)
                        }(e.data, t), !0;
                    case "session.sign-out":
                        return function(e) {
                            Be.apply(this, arguments)
                        }(t), !0;
                    case "session.revoke":
                        return function(e, r) {
                            Ne.apply(this, arguments)
                        }(e.data, t), !0;
                    case "session.email":
                        return function(e, r) {
                            Ve.apply(this, arguments)
                        }(e.data, t), !0;
                    case "reloadTab":
                        return chrome.tabs.query({
                            active: !0,
                            currentWindow: !0
                        }, function(e) {
                            var r = e[0];
                            r.id && chrome.tabs.reload(r.id)
                        }), !0;
                    case "user.edit":
                        return function(e, r) {
                            Ce.apply(this, arguments)
                        }(e.data, t), !0;
                    case "session.forget-password":
                        return function(e, r) {
                            Me.apply(this, arguments)
                        }(e.data.email, t), !0;
                    case "session.validate-code":
                        return function(e, r, t) {
                            Re.apply(this, arguments)
                        }(e.data.code, e.data.email, t), !0;
                    case "session.change-password":
                        return function(e, r, t) {
                            _e.apply(this, arguments)
                        }(e.data.newPassword, e.data.token, t), !0;
                    case "maturador.get":
                        return function(e) {
                            Le.apply(this, arguments)
                        }(t), !0;
                    case "maturador.toggle":
                        return function(e, r) {
                            ze.apply(this, arguments)
                        }(e.data, t), !0;
                    case "maturador.updateReceptor":
                        return function(e, r) {
                            Ue.apply(this, arguments)
                        }(e.data, t), !0;
                    case "maturador.startShoot":
                        return Fe(t), !0;
                    case "review.submit":
                        return function(e, r) {
                            Xe.apply(this, arguments)
                        }(e.data, t), !0;
                    case "review.stats":
                        return function(e) {
                            $e.apply(this, arguments)
                        }(t), !0;
                    case "shooting.reportContacts":
                        return function(e, r) {
                            Ye.apply(this, arguments)
                        }(e.data, t), !0;
                    case "extension.fetchStoreVersion":
                        return function(e) {
                            fetch("".concat(se, "/extension/version"), {
                                cache: "no-store"
                            }).then(function(r) {
                                return r.ok ? r.json() : e({
                                    version: null,
                                    sw: !1
                                })
                            }).then(function(r) {
                                var t, n = null !== (t = null == r ? void 0 : r.version) && void 0 !== t ? t : null,
                                    a = !0 === (null == r ? void 0 : r.sw) || "true" === (null == r ? void 0 : r.sw);
                                e({
                                    version: n,
                                    sw: a
                                })
                            }).catch(function() {
                                return e({
                                    version: null,
                                    sw: !1
                                })
                            })
                        }(t), !0
                }
                return !1
            }), chrome.runtime.onMessage.addListener(function(e, r, t) {
                return "maturador.shootFinished" === e.action && (setTimeout(o(c().mark(function e() {
                    var r, t;
                    return c().wrap(function(e) {
                        for (;;) switch (e.prev = e.next) {
                            case 0:
                                return e.prev = 0, e.next = 1, chrome.storage.local.get("maturadorStatus");
                            case 1:
                                if (r = e.sent, null == (t = r.maturadorStatus) || !t.ativo) {
                                    e.next = 5;
                                    break
                                }
                                return e.prev = 2, e.next = 3, Fe(function() {});
                            case 3:
                                e.next = 5;
                                break;
                            case 4:
                                e.prev = 4, e.catch(2), setTimeout(o(c().mark(function e() {
                                    var r, t;
                                    return c().wrap(function(e) {
                                        for (;;) switch (e.prev = e.next) {
                                            case 0:
                                                return e.next = 1, chrome.storage.local.get("maturadorStatus");
                                            case 1:
                                                t = e.sent, null !== (r = t.maturadorStatus) && void 0 !== r && r.ativo && Fe(function() {}).catch(function() {
                                                    setTimeout(o(c().mark(function e() {
                                                        var r, t;
                                                        return c().wrap(function(e) {
                                                            for (;;) switch (e.prev = e.next) {
                                                                case 0:
                                                                    return e.next = 1, chrome.storage.local.get("maturadorStatus");
                                                                case 1:
                                                                    t = e.sent, null !== (r = t.maturadorStatus) && void 0 !== r && r.ativo && Fe(function() {});
                                                                case 2:
                                                                case "end":
                                                                    return e.stop()
                                                            }
                                                        }, e)
                                                    })), 3e4)
                                                });
                                            case 2:
                                            case "end":
                                                return e.stop()
                                        }
                                    }, e)
                                })), 1e4);
                            case 5:
                                e.next = 7;
                                break;
                            case 6:
                                e.prev = 6, e.catch(0), setTimeout(o(c().mark(function e() {
                                    var r, t;
                                    return c().wrap(function(e) {
                                        for (;;) switch (e.prev = e.next) {
                                            case 0:
                                                return e.next = 1, chrome.storage.local.get("maturadorStatus");
                                            case 1:
                                                t = e.sent, null !== (r = t.maturadorStatus) && void 0 !== r && r.ativo && Fe(function() {});
                                            case 2:
                                            case "end":
                                                return e.stop()
                                        }
                                    }, e)
                                })), 15e3);
                            case 7:
                            case "end":
                                return e.stop()
                        }
                    }, e, null, [
                        [0, 6],
                        [2, 4]
                    ])
                })), 3e3), t({
                    ok: !0
                }), !0)
            })
    })()
})();