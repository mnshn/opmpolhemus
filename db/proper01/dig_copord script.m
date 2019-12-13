raw=fiff_setup_read_raw('test_opm_12_12_19.fif',1); % from MNE-matlab toolbox

n=numel(raw.info.dig);
M=zeros(n,3);
for k=1:n
    M(k,:)=raw.info.dig(k).r;
end

dlmwrite('point.txt',M,'delimiter','\t','precision','%.6f')
