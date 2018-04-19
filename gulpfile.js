const gulp  = require('gulp')
      ,gutil = require('gulp-util')
      ,fs    = require('fs')
      ,{ exec, spawn } = require('child_process');

gulp.task('default', () => {
    return gutil.log('Gulp is running')
});

gulp.task('auth-build', (cb) => {
    exec('sqlite3 db/data.db < src/db/auth.sql', (err, stdout, stderr) => {
        console.log(stdout);
        console.log(stderr);
        cb(err);
    })
});

gulp.task('tweet-build', ['auth-build'], (cb) => {
    exec('sqlite3 db/data.db < src/db/tweet.sql', (err, stdout, stderr) => {
        console.log(stdout);
        console.log(stderr);
        cb(err);
    })
});

gulp.task('run-dry-test', (cb) => {
    process.env.FLASK_APP = 'runner.py';
    const t = spawn('flask', ['run'], {stdio: 'inherit'});
    t.on('error', (err) => {
        console.log(err);
        cb(err);
    })
});

gulp.task('run-test', ['tweet-build', 'run-dry-test'], () => { })

gulp.task('db-clean', () => {
    fs.unlinkSync('db/data.db');
});