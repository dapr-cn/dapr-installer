# Dapr CLI Installer

## Windows

### Get the latest stable version

```powershell
$params = @{
  CustomAssetPrefix = 'https://ghproxy.com/https://github.com/dapr/cli/releases/download'
  DaprReleaseJson = 'https://gitee.com/dapr-cn/dapr-bin-mirror/raw/main/cli/releases.json';
}
$script=iwr -useb https://cdn.jsdelivr.net/gh/dapr-cn/dapr-installer/installer/install.ps1;
$block=[ScriptBlock]::Create(".{$script} $(&{$args} @params)");
Invoke-Command -ScriptBlock $block
```

### Get the specific version

```powershell
$params = @{
  CustomAssetPrefix = "https://ghproxy.com/https://github.com/dapr/cli/releases/download";
  DaprReleaseJson = "https://gitee.com/dapr-cn/dapr-bin-mirror/raw/main/cli/releases.json";
  Version = <Version>
}
$script=iwr -useb https://cdn.jsdelivr.net/gh/dapr-cn/dapr-installer/installer/install.ps1;
$block=[ScriptBlock]::Create(".{$script} $(&{$args} @params)");
Invoke-Command -ScriptBlock $block
```

## MacOS

### Get the latest stable version

```
curl -fsSL https://raw.githubusercontent.com/dapr/cli/master/install/install.sh | /bin/bash
```

### Get the specific version

```
curl -fsSL https://raw.githubusercontent.com/dapr/cli/master/install/install.sh | /bin/bash -s <Version>
```

## Linux

### Get the latest stable version

```
wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
```

### Get the specific version

```
wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash -s <Version>
```