const express = require('express')
const app = express()

app.get('/:tagId', (req, res) => {
  console.log(req.params.tagId)
  var tag = req.params.tagId
  var regex = /,(?![^(]*\)) /;
  try {
  let runPy = new Promise(function(success, nosuccess) {

    const { spawn } = require('child_process');
    const pyprog = spawn('python', ['./PyE3Access.py', tag]);

    pyprog.stdout.on('data', function(data) {

        success(data);
        pyprog.kill()
    });

    pyprog.stderr.on('data', (data) => {

        nosuccess(data);
        pyprog.kill()
    });
});
        runPy.then(function(fromRunpy) {
            var response = fromRunpy.toString().split(regex)
            console.log(response);
            res.end(response[2].toString());
        });
    } catch(error) {
        console.log(error)
    }
})

app.listen(7834, () => console.log('Application listening on port 7834!'))