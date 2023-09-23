const cp = require('child_process');

var progs = {
    list:'ls',
    copy: 'cp',
    folder: 'mkdir'
}

var child = cp.spawn(progs.list, ["-a"], {cwd:".."});
child.stdout.on ('data', (data) => {
  console.log(`data\n${data}`)  
});

child.stderr.on('data', (err) => {
    console.log(`error\n${err}`)
})