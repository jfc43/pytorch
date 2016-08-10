import torch
from torch.legacy import nn

class Transpose(nn.Module):
    # transpose dimensions:
    # n = nn.Transpose({1, 4}, {1, 3})
    # will transpose dims 1 and 4,: 1 and 3...

    def __init__(self, *args):
        super(Transpose, self).__init__()
        self.permutations = args

    def updateOutput(self, input):
        for perm in self.permutations:
           input = input.transpose(*perm)
        self.output.resizeAs_(input).copy(input)
        return self.output

    def updateGradInput(self, input, gradOutput):
        for perm in self.permutations[::-1]:
           gradOutput = gradOutput.transpose(*perm)
        self.gradInput.resizeAs_(gradOutput).copy(gradOutput)
        return self.gradInput


