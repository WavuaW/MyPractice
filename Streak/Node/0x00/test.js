const cp = require('child_process')

const progs = {
    list:'ls',
    copy: 'cp',
    folder: 'mkdir'
}

var child = cp.spawn(progs.list)

child.stdout.on ('data', (data) => {
  console.log(`data\n${data}`)  
})
