/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.drill.exec.planner.logical;

import org.eigenbase.rel.rules.PushProjector;
import org.eigenbase.rex.RexCall;
import org.eigenbase.rex.RexNode;

public final class DrillConditions {

  public static PushProjector.ExprCondition PRESERVE_ITEM = new PushProjector.ExprCondition() {
    @Override
    public boolean test(RexNode expr) {
      if (expr instanceof RexCall) {
        RexCall call = (RexCall)expr;
        return "item".equals(call.getOperator().getName().toLowerCase());
      }
      return false;
    }
  };
}