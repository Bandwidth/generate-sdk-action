exists=$(hub pr list -h temp-ci-cd-test)
if [ -z "exists" ]
then
echo "dont do a barrel roll"
else
echo "do a barrel roll"
fi
