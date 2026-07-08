
### first steps

installation
"""
npm init -y  // creates a package.json
npm pkg set type=module // sets type:module so you use import/export (not old require)
npm install -D typescript
"""


adding the tsconfig.json
"""
npx tsc --init
"""


"""
changing the /Users/josescoppola/Documents/sandbox/ts-path/101/package.json to run: << run the typescript checker over all my .ts files and report any type errors>>
npm pkg set scripts.typecheck="tsc --noEmit"
npm run typecheck
"""