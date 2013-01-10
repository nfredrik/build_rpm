Name            : helloworld
Summary         : Hello world application

#The version line should be set to the version of the software being packaged. 
#The version will also be included in the package label, and the package filename. 
Version         : %{?TAGNAME}

#The release is a number that is used to represent the number of times the software,
#at the present version, has been packaged. You can think of it as the package's version number.
# The release is also part of the package label and package filename. 
Release         : %{?BUILD_NUMBER}

Group		: Applications/File
License		: (c) Douglas Gibbons
BuildArch       : noarch
BuildRoot       : %{_tmppath}/%{name}-%{version}-root

# Use "Requires" for any dependencies, for example:
# Requires        : tomcat6

# Description gives information about the rpm package. This can be expanded up to multiple lines.
%description
Hello World app


# Prep is used to set up the environment for building the rpm package
# Expansion of source tar balls are done in this section
%prep

# Used to compile and to build the source
%build

# The installation. 
# We actually just put all our install files into a directory structure that mimics a server directory structure here
%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/usr/bin/
cp ../SOURCES/helloworld.sh $RPM_BUILD_ROOT/usr/bin/.

# Contains a list of the files that are part of the package
# See useful directives such as attr here: http://www.rpm.org/max-rpm-snapshot/s1-rpm-specref-files-list-directives.html
%files
%attr(755, root, -) /usr/bin/helloworld.sh
/usr/bin/helloworld.sh

# Used to store any changes between versions
%changelog
