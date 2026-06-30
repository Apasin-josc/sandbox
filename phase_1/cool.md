package.json = your shopping list, in your handwriting: "a dozen eggs (any brand), milk (any 2%)." It's your intent, and it's flexible.
package-lock.json = the receipt from the trip: "Eggland eggs, lot #1234, $4.99, from this exact shelf." It records exactly what you actually got.

So: package.json = what you want (human-authored). package-lock.json = what you got (machine-generated, never hand-edited). You need both — one is the source of intent, the other is the reproducible snapshot.



node --watch server.js