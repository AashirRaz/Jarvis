import pip

__all__ = [
    "attrs>=23.2.0",
    "beautifulsoup4>=4.12.3",
    "certifi>=2024.2.2",
    "charset-normalizer>=3.3.2",
    "h11>=0.14.0",
    "idna>=3.6",
    "outcome>=1.3.0.post0",
    "pyobjc-core>=10.1",
    "pyobjc-framework-Cocoa>=10.1",
    "PySocks>=1.7.1",
    "requests>=2.31.0",
    "selenium>=4.18.1",
    "setuptools>=69.1.1",
    "SkPy>=0.10.6",
    "sniffio>=1.3.1",
    "sortedcontainers>=2.4.0",
    "soupsieve>=2.5",
    "trio>=0.24.0",
    "trio-websocket>=0.11.1",
    "typing_extensions>=4.10.0",
    "urllib3>=2.2.1",
    "wheel>=0.42.0",
    "wsproto>=1.2.0",
    "inquirer>=3.2.4"
]

windows = ["win11toast>=0.34"]
darwin = ["macos-notifications>=0.2.0"]


def install(packages:list[str]) -> None:
    for package in packages:
        pip.main(["install", package])


if __name__ == "__main__":
    from Constants import OS
    
    install(__all__)
    install(darwin if OS.IOS else windows)


