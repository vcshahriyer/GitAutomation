const { exec, execSync } = require("child_process");
const readline = require("readline");
var readlineSync = require('readline-sync');
const open = require("open")
// Default variables
const _remote = "origin";

const run = (arg) => {
  try {
    return execSync(`git ${arg}`);
  } catch(err){
    return err;
  }
};

const gitRemoteInfo = () => {
    const cmd = run("remote -v");
    const output = cmd.toString(); 
    const parse = output.split(" ");
    const match = /com[:\/](.+).git$/g.exec(parse[0]);
    const [userName, repoName] = match[1].split("/");
    return ({ userName, repoName });
};

const getActiveBranchName = () => {
    const cmd = run("branch");
    const output = cmd.toString();
    const parse = /(\*)([\s\w]+)/g.exec(output);
    const branch = parse[2];
    return (branch.trim());
};

const getAllLocalBranchName = () => {
  return new Promise((resolve, reject) => {
    const cmd = run("branch");
    cmd.stdout.on("data", (output) => {
      const parse = output.split(" ");
      const branches = [];
      for (item of parse) {
        if (item === "*" || item === "") {
          continue;
        }
        branches.push(item.trim());
      }
      resolve(branches);
    });
  });
};

const getAllRemoteBranchName = (remote) => {
  return new Promise((resolve, reject) => {
    const cmd = run("branch -r");
    cmd.stdout.on("data", (output) => {
      const parse = output.split(" ");
      let remoteBranches = [];
      for (item of parse) {
        if (item.includes(`${remote}/`) && !item.includes("HEAD")) {
          remoteBranches.push(item.split("/")[1].trim());
        }
      }
      resolve(remoteBranches);
    });
  });
};

const add = () => {
  run("add -A");
};

const commit = (message) => {
  if (!message) {
    const read = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    read.question("Type in your commit message: ", (answer) => {
      run(`commit -am "${answer}"`);
      read.close();
    });
  }
};

const branch = (name) => {
   return run(`checkout -b ${name}`);
};

const fetch = (remote) => {
  run(`fetch ${remote}`);
};

const pull = (remote, b_name=null) => {
  if(!b_name) {
    getActiveBranchName().then(branchName=>{
    run(`pull ${remote} ${branchName}`);
  })}else{
    run(`pull ${remote} ${b_name}`);
  }
  
}

const push = (remote, b_name=null) => {
  if(!b_name) {
    const branchName = getActiveBranchName();
    run(`push -u ${remote} ${branchName}`);
  }else{
    run(`push -u ${remote} ${b_name}`);
  }
  
}


const deleteBranch = (b_name, force) => {
    if (force)
        run(`branch -D ${b_name}`)
    else
        run(`branch -d ${b_name}`)
}

const pruneRemote = async (force=false, remote) =>{
    // fetch(remote)
    localBranches = await getAllLocalBranchName()

    const cmd = run(`remote prune ${remote}`);
    cmd.stdout.on("data", (output) => {
      const parse = output.split(" ");
      for (pruned of parse) {
        if (pruned.includes(`${remote}/`)) {
          const {origin, branch} = pruned.split("/")
          if(localBranches.includes(branch))
            console.log(branch)
        }
      }
    });
}
const pruneLocal = async (force=false, remote) =>{
    fetch(remote)
    localBranches = await getAllLocalBranchName()
    run(`remote prune ${remote}`)
    remoteBranches = await getAllRemoteBranchName(remote)

      for (br of localBranches) {
        if (!remoteBranches.includes(br)) {
            console.log(`Deleted Branch: ${br}`)
            deleteBranch(br)
        }
      }
}

const sync = (remote) => {
    fetch(remote)
    pull(remote)
}
const justNewBranchPushPR = (remote) => {
    const {userName, repoName} = gitRemoteInfo()
    const b_name = readlineSync.question('Type in the name of the branch you want to make: ');
    url = `https://github.com/${userName}/${repoName}/pull/new/${b_name}`
    console.log(url);
    branch(b_name)
    push(remote, b_name)
    // const branch = run(`checkout -b ${b_name}`)
    // branch.stdout.on("data", (bout)=> {
    //   console.log(bout)
    //   const push = run(`push -u ${remote} ${b_name}`)
    //     push.stdout.on("data", (pout)=>{
    //       open(url)
    //     })
    // })
}

// push('origin')
// justNewBranchPushPR('origin');
pruneLocal(false, 'origin')
