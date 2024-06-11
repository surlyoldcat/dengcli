# deng
deng is your friend. not an evil venomous space badger.

## Project Layout
this is pretty rough, but the idea is to keep the 'root' CLI pretty clean and simple, and register 'groups' for different domains. e.g. for Datashares and OpenMetadata and whatever else.

In this thing, i just have subcommands set up for OpenMetadata and Datashares.

For the moment, I am making the assumption that there will be one 'config' file per dataset, and the various commands will just need to be fed a filename.  The 'config directory' in the env should point to the folder containing all those files. It's pretty likely if this thing expands much, each 'plugin' package will have to manage its own special configs, but that would be overkill at this point.
## Runnit
Very rough instructions
1. Copy/update the sample_env.txt file and name it `.env`
2. Set up a virtual env for this thingy, and install `boto3` and `click`
3. Activate the venv and do a `pip install --editable .`
4. Then you should be able to do `deng` from the command line.

## Examples
- `deng datashare delete myDatashare.yaml --cascade `
- `deng datashare create yourDatashare.yaml  --prompt`
- `deng openmetadata publish myOtherDatashare.yaml`
- `deng datashare` should just list all the files in the config dir
